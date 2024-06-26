from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr

    postgres_host: str
    postgres_db: str
    postgres_password: str
    postgres_port: str
    postgres_user: str

    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    def build_postgres_dsn(self) -> str:
        return (
            "postgresql+psycopg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )