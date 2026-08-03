from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from rubikstock_api.core.config import Settings, get_settings
from rubikstock_api.db.session import check_database
from rubikstock_api.schemas.meta import HealthResponse, ReadinessResponse, ServiceInfo

router = APIRouter(tags=["system"])


@router.get("/healthz", response_model=HealthResponse, summary="Health check")
def healthz(settings: Annotated[Settings, Depends(get_settings)]) -> HealthResponse:
    return HealthResponse(
        name=settings.app_name,
        environment=settings.app_env,
        version=settings.app_version,
    )


@router.get("/readyz", response_model=ReadinessResponse, summary="Readiness check")
def readyz(settings: Annotated[Settings, Depends(get_settings)]) -> ReadinessResponse:
    database_ok, detail = check_database(settings.database_url)
    if not database_ok:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "degraded",
                "database": "down",
                "detail": detail,
            },
        )

    return ReadinessResponse(
        name=settings.app_name,
        environment=settings.app_env,
        version=settings.app_version,
        database="ok",
    )


@router.get("/meta", response_model=ServiceInfo, summary="Service metadata")
def meta(settings: Annotated[Settings, Depends(get_settings)]) -> ServiceInfo:
    return ServiceInfo(
        name=settings.app_name,
        environment=settings.app_env,
        version=settings.app_version,
    )
