import uuid

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    password: str

class PublicUserReturnSchema(BaseModel):
    id: uuid.UUID
    username: str
