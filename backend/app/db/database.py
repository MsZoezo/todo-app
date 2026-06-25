from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from . import models  # type: ignore  # noqa: F401, PGH003

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session]:
    with Session(engine) as session:
        yield session
