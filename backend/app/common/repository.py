from collections.abc import Sequence
from typing import Generic, TypeVar

from sqlmodel import SQLModel, select
from sqlmodel.sql.expression import SelectOfScalar

from app.db.dependencies import SessionDep

T = TypeVar("T", bound=SQLModel)
S = TypeVar("S", bound=SQLModel)

class BaseRepository(Generic[T]):
    def __init__(self, session: SessionDep, model: type[T]) -> None:
        """Initialize base reposity with session dependency."""
        self.session = session
        self.model = model

    def query_select(self) -> SelectOfScalar[T]:
        return select(self.model)

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)

        return obj

    async def update(self, obj: T, scheme: SQLModel) -> T:
        obj.sqlmodel_update(scheme.model_dump(exclude_unset=True))

        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)

        return obj

    async def delete(self, obj: T) -> None:
        self.session.delete(obj)
        self.session.commit()

    async def get_all(self) -> Sequence[T]:
        return self.session.exec(select(self.model)).all()
