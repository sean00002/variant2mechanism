"""The Anthropic API transport: the client's chat-completions body sent to the Messages API with the official SDK, and
the reply returned in chat-completions form, so the response cache, budget and trace work as they do for OpenRouter.

The key comes only from V2M_ANTHROPIC_API_KEY and is passed to the SDK explicitly: the name ANTHROPIC_API_KEY is left
to other tools on the same machine. The key is never printed or logged, and the base URL is fixed, so an
ANTHROPIC_BASE_URL set for another tool is not used either. Effort and the strict JSON schema go in `output_config`; no
`thinking` is sent, so Claude Opus 5 thinks adaptively, its default. v8 sends no tools, and this transport sends none.

With `cache_system` the system text is marked for the API's prompt cache (5 minutes). A client that sends the same
instructions with every call then pays their full price once, and the cached price while the calls keep coming. Only
what the call costs changes: the request the model reads is the same, and so is the response cache's key.
"""

import os

import anthropic

from .llm import LLMError, MissingKey

KEY_VAR = "V2M_ANTHROPIC_API_KEY"
URL = "https://api.anthropic.com"
FINISH = {"end_turn": "stop", "stop_sequence": "stop", "max_tokens": "length", "refusal": "content_filter"}
PROVIDER = "Anthropic API"          # in the trace, apart from OpenRouter's own provider called "Anthropic"


def to_messages(body: dict, cache_system: bool = False) -> dict:
    """The Messages API parameters for a chat-completions body: system messages on top, the rest as they are. With
    `cache_system` the system text is one block marked for the prompt cache."""
    if body.get("tools") or any(m["role"] not in ("system", "user", "assistant") or m.get("tool_calls")
                                for m in body["messages"]):
        raise LLMError("the Anthropic API transport sends text stages only; this call has tools")
    params = {"model": body["model"], "max_tokens": body["max_tokens"],
              "messages": [{"role": m["role"], "content": m["content"]} for m in body["messages"]
                           if m["role"] != "system"]}
    system = "\n\n".join(m["content"] for m in body["messages"] if m["role"] == "system")
    if system:
        params["system"] = ([{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}]
                            if cache_system else system)
    out = {}
    if (body.get("reasoning") or {}).get("effort"):
        out["effort"] = body["reasoning"]["effort"]
    if body.get("response_format"):
        out["format"] = {"type": "json_schema", "schema": body["response_format"]["json_schema"]["schema"]}
    if out:
        params["output_config"] = out
    return params


def to_chat(msg) -> dict:
    """A Messages API reply in chat-completions form. A refusal keeps its category and explanation in
    `message.refusal`; the thinking blocks are left out (their text is empty by default)."""
    message = {"role": "assistant", "content": "".join(b.text for b in msg.content if b.type == "text")}
    if msg.stop_reason == "refusal" and msg.stop_details:
        message["refusal"] = f"{msg.stop_details.category}: {msg.stop_details.explanation}"
    u = msg.usage
    cached, written = u.cache_read_input_tokens or 0, u.cache_creation_input_tokens or 0
    usage = {"prompt_tokens": u.input_tokens + cached + written, "completion_tokens": u.output_tokens,
             "prompt_tokens_details": {"cached_tokens": cached, **({"cache_write_tokens": written} if written else {})}}
    if u.output_tokens_details:
        usage["completion_tokens_details"] = {"reasoning_tokens": u.output_tokens_details.thinking_tokens}
    return {"id": msg.id, "model": msg.model, "provider": PROVIDER, "usage": usage,
            "choices": [{"message": message, "finish_reason": FINISH.get(msg.stop_reason, msg.stop_reason)}]}


def anthropic_transport(max_tries: int = 4, timeout: int = 900, client=None, cache_system: bool = False):
    """Streams each call (generate may ask for 64,000 tokens after a max_tokens retry). The SDK retries 429, 5xx
    and connection errors before a reply starts, up to `max_tries` attempts in all. `cache_system`: see the module
    docstring."""
    if client is None:
        key = os.environ.get(KEY_VAR)
        if not key:
            raise MissingKey(f"{KEY_VAR} is not set. Export it in the shell that starts the run.")
        client = anthropic.Anthropic(api_key=key, base_url=URL, max_retries=max_tries - 1, timeout=timeout)

    def send(body: dict) -> dict:
        try:
            with client.messages.stream(**to_messages(body, cache_system)) as stream:
                return to_chat(stream.get_final_message())
        except anthropic.APIStatusError as e:
            raise LLMError(f"Anthropic API error {e.status_code}: {str(e.message)[:300]}") from None
        except anthropic.APIConnectionError as e:
            raise LLMError(f"Anthropic API call failed ({type(e).__name__})") from None

    return send
