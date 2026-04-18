from contextlib import asynccontextmanager
from database import engine, Model
from fastapi import FastAPI
from routers.crud import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    yield

    print("Сервер выключен!")

app = FastAPI(
    title="Менеджер книг API",
    description="Создавайте, читайте, обновляйте и удаляйте книги",
    version="1.0.0",
    lifespan=lifespan)

app.include_router(router)
