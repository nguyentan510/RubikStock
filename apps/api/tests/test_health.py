from __future__ import annotations

from fastapi.testclient import TestClient

from rubikstock_api.main import create_app


def test_health_and_meta_endpoints(monkeypatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    monkeypatch.setenv("APP_ENV", "local")
    monkeypatch.setenv("APP_VERSION", "0.1.0")
    app = create_app()

    with TestClient(app) as client:
        health = client.get("/api/v1/healthz")
        assert health.status_code == 200
        assert health.json()["status"] == "ok"
        assert health.json()["name"] == "RubikStock API"

        ready = client.get("/api/v1/readyz")
        assert ready.status_code == 200
        assert ready.json()["database"] == "ok"

        meta = client.get("/api/v1/meta")
        assert meta.status_code == 200
        assert meta.json()["version"] == "0.1.0"


def test_root_and_openapi(monkeypatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    app = create_app()
    with TestClient(app) as client:
        root = client.get("/")
        assert root.status_code == 200
        assert root.json()["health"] == "/api/v1/healthz"

        openapi = client.get("/openapi.json")
        assert openapi.status_code == 200
        payload = openapi.json()
        assert payload["info"]["title"] == "RubikStock API"
        assert "/api/v1/healthz" in payload["paths"]
