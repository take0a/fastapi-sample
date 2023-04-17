from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from . import config


settings = config.Settings()
DB_URL = "postgresql+asyncpg://" \
    f"{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:5432/postgres"

engine = create_async_engine(DB_URL, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with async_session() as session:
        yield session
