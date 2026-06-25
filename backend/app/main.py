from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .core.api import routers
from .db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:  # noqa: ARG001
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
