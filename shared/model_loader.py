"""Model import helpers."""

from __future__ import annotations


def load_models() -> None:
    import services.auth_service.models  # noqa: F401
    import services.catalog_service.models  # noqa: F401
    import services.circulation_service.models  # noqa: F401
