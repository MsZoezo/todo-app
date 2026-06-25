from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db.database import init_db
from .users.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:  # noqa: ARG001
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router=router)

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
