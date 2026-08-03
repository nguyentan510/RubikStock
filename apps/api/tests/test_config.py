from __future__ import annotations

from rubikstock_api.core.config import Settings


def test_allowed_origins_accepts_comma_separated_env(monkeypatch) -> None:
    monkeypatch.setenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000",
    )

    settings = Settings(_env_file=None)

    assert settings.allowed_origins == [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
