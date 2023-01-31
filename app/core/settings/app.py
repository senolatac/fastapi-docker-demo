import logging
from typing import Any, Dict

from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = True
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.0.0"

    admin_key_token: str = "admin"
    secure_key_token: str = "user1,user2"

    logging_level: int = logging.DEBUG

    """configuration"""
    class Config:
        validate_assignment = True

    @property
    def connect_ags(self) -> Dict[str, Any]:
        return {}

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
