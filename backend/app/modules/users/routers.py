import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from app.core.exceptions import InstanceNotFoundError, InstanceUniqueConstraintError

from .dependencies import UserServiceDep
from .schemas import PublicUserReturnSchema, UserCreateSchema

router = APIRouter(prefix="/users")

@router.post("/create", response_model=PublicUserReturnSchema)
async def create_user(user_data: UserCreateSchema, service: UserServiceDep) -> Any:
    try:
        return await service.create_user(user_data)
    except InstanceUniqueConstraintError as err:
        raise HTTPException(404, "Name already in use.") from err

@router.get("/", response_model=list[PublicUserReturnSchema])
async def get_users(service: UserServiceDep) -> Any:
    return await service.get_users()

@router.get("/{user_id}", response_model=PublicUserReturnSchema)
async def get_one_user(user_id: uuid.UUID, service: UserServiceDep) -> Any:
    try:
        return await service.get_user(user_id)
    except InstanceNotFoundError as err:
        raise HTTPException(404, "No user with that id.") from err
