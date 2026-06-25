from typing import Annotated

from fastapi import Depends

from .services import UserService, get_user_service

UserServiceDep = Annotated[UserService, Depends(get_user_service)]
