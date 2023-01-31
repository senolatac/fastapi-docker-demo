from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    """configuration"""
    class Config(AppSettings.Config):
        env_file = "prod.env"
