"""Load config.yaml and resolve its paths.

Relative paths are relative to the repo root; `~` is expanded. Set V2M_CONFIG to use another file.
"""

import os
from functools import lru_cache
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]


class ConfigError(ValueError):
    """Raised when config.yaml is missing a value or still has an ASK placeholder."""


class Config(dict):
    """A dict of sections with a `path()` helper for local file paths."""

    def path(self, section: str, key: str) -> Path:
        value = self[section][key]
        if value in (None, "", "ASK"):
            raise ConfigError(f"config.yaml: {section}.{key} is not set")
        p = Path(os.path.expanduser(str(value)))
        return p if p.is_absolute() else REPO / p

    def remote(self, section: str, key: str) -> str:
        """A cluster path or value, checked but not resolved locally."""
        value = self[section][key]
        if value in (None, "", "ASK"):
            raise ConfigError(f"config.yaml: {section}.{key} is not set")
        return str(value)


def _merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for k, v in over.items():
        out[k] = _merge(base[k], v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return out


def with_profile(cfg: Config, name: str | None) -> Config:
    """cfg with `profiles.<name>` merged over it key by key (a new Config); cfg itself when name is None."""
    if not name:
        return cfg
    profiles = cfg.get("profiles") or {}
    if name not in profiles:
        raise ConfigError(f"config.yaml: no profile '{name}' (have: {', '.join(profiles) or 'none'})")
    return Config(_merge(cfg, profiles[name]))


@lru_cache(maxsize=4)
def load_config(path: str | None = None) -> Config:
    path = path or os.environ.get("V2M_CONFIG") or str(REPO / "config.yaml")
    with open(path) as f:
        return Config(yaml.safe_load(f))
