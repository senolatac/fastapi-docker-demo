import logging
from typing import Dict, Any

from pydantic import SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test_secret")

    logging_level: int = logging.DEBUG

    """configuration"""
    class Config(AppSettings.Config):
        env_file = "test.env"

    @property
    def connect_ags(self) -> Dict[str, Any]:
        return {
            "check_same_thread": False
        }
