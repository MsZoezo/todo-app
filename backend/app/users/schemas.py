import uuid

from sqlmodel import SQLModel


class UserCreateSchema(SQLModel):
    username: str
    password: str

class PublicUserReturnSchema(SQLModel):
    id: uuid.UUID
    username: str
