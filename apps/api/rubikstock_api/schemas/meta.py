from __future__ import annotations

from pydantic import BaseModel, Field


class ServiceInfo(BaseModel):
    name: str
    environment: str
    version: str


class HealthResponse(ServiceInfo):
    status: str = Field(default="ok")


class ReadinessResponse(ServiceInfo):
    status: str = Field(default="ok")
    database: str
    detail: str | None = None

