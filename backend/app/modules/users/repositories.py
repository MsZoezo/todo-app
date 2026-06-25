import uuid
from typing import Union

from sqlmodel import select

from app.common.repository import BaseRepository

from .models import User


class UserRepository(BaseRepository[User]):
    def get_by_id(self, user_id: uuid.UUID) -> Union[User, None]:
        return self.session.exec(select(User).where(User.id == user_id)).one_or_none()

    def get_by_username(self, username: str) -> Union[User, None]:
        return self.session.exec(select(User).where(User.username == username)).one_or_none()
