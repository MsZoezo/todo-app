import uuid

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.auth.utils import hash_password
from app.db.dependencies import SessionDep

from .models import User
from .schemas import PublicUserReturnSchema, UserCreateSchema

router = APIRouter(prefix="/users")

@router.post("/create")
async def create_user(user_data: UserCreateSchema, session: SessionDep) -> PublicUserReturnSchema:
    if session.exec(select(User).where(User.username == user_data.username)).one_or_none():
        raise HTTPException(400, "Username already in use.")

    user = User (
        username=user_data.username,
        password=hash_password(user_data.password)
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return PublicUserReturnSchema.model_validate(user)

@router.get("/")
async def get_users(session: SessionDep) -> list[PublicUserReturnSchema]:
    users = session.exec(select(User)).all()

    return [PublicUserReturnSchema.model_validate(user) for user in users]

@router.get("/{user_id}")
async def get_one_user(user_id: uuid.UUID, session: SessionDep) -> PublicUserReturnSchema:
    user = session.exec(select(User).where(User.id == user_id)).one_or_none()

    if not user:
        raise HTTPException(404, "No user with that id.")

    return PublicUserReturnSchema.model_validate(user)
