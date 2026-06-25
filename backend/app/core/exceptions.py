
from typing import TypeVar

from sqlmodel import SQLModel

T = TypeVar("T", bound=SQLModel)

class InstanceNotFoundError(Exception):
    def __init__(self, model: type[T]) -> None:
        """Initialize exception."""
        super().__init__(f"Instance for `{model.__name__}` not found.")

class InstanceUniqueConstraintError(Exception):
    def __init__(self, model: type[T], field: str, key: str) -> None:
        """Initialize exception."""
        super().__init__(
            f"Existing instance for `{model.__name__}` with key `{key}` for unique field `{field}`"
        )
