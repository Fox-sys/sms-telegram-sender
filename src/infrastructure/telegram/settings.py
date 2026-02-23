from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TELEGRAM_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    BOT_TOKEN: str
    CHAT_ID: str
