from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    DB_URL: str
    DB_ECHO: bool = False
    DB_LOGGING_LEVEL: str = "INFO"

    @property
    def LOGGING_CONFIG(self) -> dict:
        config: dict = {
            "loggers": {
                "alembic": {
                    "handlers": ["default"],
                    "level": self.LOGGING_LEVEL,
                    "propagate": False,
                }
            }
        }
        if self.DB_ECHO:
            config["loggers"]["sqlalchemy"] = {
                "handlers": ["default"],
                "level": self.LOGGING_LEVEL,
                "propagate": False,
            }
        return config


class AlembicSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ALEMBIC_",
        extra="ignore",
    )
    ALEMBIC_SCRIPT_LOCATION: str = "src/infrastructure/database/alembic"
    ALEMBIC_VERSION_LOCATIONS: str = "src/infrastructure/database/migration"
    ALEMBIC_MIGRATION_FILENAME_TEMPLATE: str = (
        "%%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d_%%(minute).2d_%%(second).2d_%%(slug)s"
    )
