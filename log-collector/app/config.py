from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    opensearch_host: str = "opensearch"
    opensearch_port: int = 9200
    index_prefix: str = "sentinel-logs"

    class Config:
        env_file = ".env"


settings = Settings()