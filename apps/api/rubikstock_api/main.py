from __future__ import annotations

import logging
import time
from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from rubikstock_api.api.v1.router import api_router
from rubikstock_api.core.config import get_settings
from rubikstock_api.core.logging import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    configure_logging(
        service_name=settings.app_name,
        environment=settings.app_env,
        level=settings.log_level,
    )
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="RubikStock API",
        version=settings.app_version,
        description="Technical foundation for RubikStock.",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def request_logging_middleware(request: Request, call_next):
        request_id = request.headers.get("x-request-id") or str(uuid4())
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - start) * 1000, 2)
        response.headers["x-request-id"] = request_id
        response.headers["x-service-name"] = settings.app_name
        response.headers["x-service-version"] = settings.app_version
        response.headers["x-app-environment"] = settings.app_env

        logger = logging.getLogger("rubikstock_api.http")
        logger.info(
            "request complete",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        return response

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/", include_in_schema=False)
    def root() -> JSONResponse:
        payload = {
            "name": settings.app_name,
            "environment": settings.app_env,
            "version": settings.app_version,
            "docs": "/docs",
            "openapi": "/openapi.json",
            "health": "/api/v1/healthz",
            "ready": "/api/v1/readyz",
        }
        return JSONResponse(payload)

    return app


app = create_app()
