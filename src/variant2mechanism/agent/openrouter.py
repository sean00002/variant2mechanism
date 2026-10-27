"""The OpenRouter transport: sends one chat-completions request and returns the reply as it came.

The key comes only from OPENROUTER_API_KEY and is never printed or logged. Requests go only to providers that
support every parameter sent (`require_parameters`), and ask for the cost to be reported (`usage.include`); the
provider that served each call is in the reply. These two are added here, outside the response-cache key.
"""

import json
import os
import random
import time

import requests

from .llm import RETRY_STATUS, LLMError, MissingKey

KEY_VAR = "OPENROUTER_API_KEY"
URL = "https://openrouter.ai/api/v1/chat/completions"


def openrouter_transport(provider: dict | None = None, max_tries: int = 4, session=None, sleep=time.sleep,
                         timeout: int = 900):
    key = os.environ.get(KEY_VAR)
    if not key:
        raise MissingKey(f"{KEY_VAR} is not set. Export it in the shell that starts the run.")
    http = session or requests.Session()
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "X-Title": "variant2mechanism"}

    def send(body: dict) -> dict:
        full = {**body, "usage": {"include": True}, "provider": {"require_parameters": True, **(provider or {})}}
        last = None
        for attempt in range(max_tries):
            try:
                r = http.post(URL, headers=headers, data=json.dumps(full), timeout=timeout)
            except requests.RequestException as e:
                last = f"connection: {type(e).__name__}"
            else:
                data = r.json() if r.text else {}
                err = data.get("error") if isinstance(data, dict) else None
                if r.status_code == 200 and not err and data.get("choices"):
                    return data
                code = (err or {}).get("code")
                code = code if isinstance(code, int) else r.status_code
                if code not in RETRY_STATUS:
                    raise LLMError(f"OpenRouter error {code}: {str((err or {}).get('message') or r.text)[:300]}")
                last = str(code)
            sleep(min(60, 2 ** attempt * 2 + random.random()))
        raise LLMError(f"OpenRouter call failed after {max_tries} tries ({last})")

    return send
