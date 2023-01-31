import logging

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    logging_level: int = logging.DEBUG

    """configuration"""
    class Config(AppSettings.Config):
        env_file = ".env"
