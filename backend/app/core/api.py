from fastapi import APIRouter

from app.modules.users.routers import router as users_router

routers: list[APIRouter] = [
    users_router
]
