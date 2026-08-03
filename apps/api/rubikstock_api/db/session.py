from __future__ import annotations

from functools import lru_cache

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker


def _engine_kwargs(database_url: str) -> dict[str, object]:
    kwargs: dict[str, object] = {
        "pool_pre_ping": True,
        "future": True,
    }
    if database_url.startswith("sqlite"):
        kwargs["connect_args"] = {"check_same_thread": False}
    return kwargs


@lru_cache(maxsize=1)
def get_engine(database_url: str) -> Engine:
    return create_engine(database_url, **_engine_kwargs(database_url))


@lru_cache(maxsize=1)
def get_session_factory(database_url: str) -> sessionmaker[Session]:
    return sessionmaker(
        bind=get_engine(database_url),
        autoflush=False,
        autocommit=False,
        future=True,
    )


def check_database(database_url: str) -> tuple[bool, str]:
    engine = get_engine(database_url)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True, "ok"
    except SQLAlchemyError as exc:
        return False, str(exc)
