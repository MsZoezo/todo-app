import uuid
from typing import Any

from fastapi import APIRouter

from .schemas import PublicUserReturnSchema, UserCreateSchema
from .services import UserServiceDep

router = APIRouter(prefix="/users")

@router.post("/create", response_model=PublicUserReturnSchema)
async def create_user(user_data: UserCreateSchema, service: UserServiceDep) -> Any:
    return await service.create_user(user_data)

@router.get("/", response_model=list[PublicUserReturnSchema])
async def get_users(service: UserServiceDep) -> Any:
    return await service.get_users()

@router.get("/{user_id}", response_model=PublicUserReturnSchema)
async def get_one_user(user_id: uuid.UUID, service: UserServiceDep) -> Any:
    return await service.get_user(user_id)
