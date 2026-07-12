from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Mini Chatbase"
    app_version: str = "1.0.0"

    debug: bool = False
    api_v1_str: str = "/api/v1"

    host: str = "127.0.0.1"
    port: int = 8000

    database_url: str 

    jwt_secret: str = ""
    openai_api_key: str = ""
    redis_url: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings() # type: ignore
