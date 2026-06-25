import uuid
from collections.abc import Sequence
from typing import Annotated

from fastapi import Depends, HTTPException

from app.auth.utils import hash_password
from app.core.exceptions import InstanceNotFoundError, InstanceUniqueConstraintError
from app.db.dependencies import SessionDep

from .models import User
from .repositories import UserRepository
from .schemas import UserCreateSchema


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        """Initialize user service."""
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreateSchema) -> User:
        if self.user_repo.get_by_username(user_data.username):
            raise InstanceUniqueConstraintError(User, "username", user_data.username)

        user = User (
            username=user_data.username,
            password=hash_password(user_data.password)
        )

        await self.user_repo.create(user)

        return user

    async def get_user(self, user_id: uuid.UUID) -> User:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise InstanceNotFoundError(User)

        return user

    async def get_users(self) -> Sequence[User]:
        return await self.user_repo.get_all()

def get_user_service(session: SessionDep) -> UserService:
    user_repo = UserRepository(session, User)

    return UserService(user_repo)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]
