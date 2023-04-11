from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from . import config


settings = config.Settings()
DB_URL = "postgresql+asyncpg://" \
    f"{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:5432/postgres"

async_engine = create_async_engine(DB_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False,
                             bind=async_engine, class_=AsyncSession)

Base = declarative_base()


async def get_session():
    async with async_session() as session:
        yield session
