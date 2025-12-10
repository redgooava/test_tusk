from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ORIGINS: list = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:3000",
    ]

    API_V1_STR: str = "/v1"
    API_V1_LINKS_STR: str = "/links"


settings = Settings()
