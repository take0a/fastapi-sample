from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str

    class Config:
        env_file = ".env.dev"
