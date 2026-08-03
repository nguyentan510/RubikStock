from __future__ import annotations

from collections.abc import Iterator

import pytest

from rubikstock_api.core.config import get_settings


@pytest.fixture(autouse=True)
def reset_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()

