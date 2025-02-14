from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from db.base_model import Model
from config import settings
import aiosqlite

# Создаем движок для SQLite
engine = create_async_engine(
    settings.get_async_uri(),  # Используем get_async_uri() для SQLite
)

# Создаем фабрику сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with new_session() as db:
        try:
            yield db
        finally:
            await db.close()

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
