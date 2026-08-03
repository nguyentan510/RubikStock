from __future__ import annotations

import json
import logging
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    def __init__(self, service_name: str, environment: str) -> None:
        super().__init__()
        self.service_name = service_name
        self.environment = environment

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "service": self.service_name,
            "environment": self.environment,
        }

        for field in ("request_id", "method", "path", "status_code", "duration_ms"):
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload, ensure_ascii=False)


def configure_logging(*, service_name: str, environment: str, level: str) -> None:
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter(service_name=service_name, environment=environment))
    root_logger.addHandler(handler)
    root_logger.setLevel(level.upper())

