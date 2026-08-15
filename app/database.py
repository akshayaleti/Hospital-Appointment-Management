"""Database configuration for the hospital management application."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///hospital.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


def get_db():
    """Create a database session and close it after use."""

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
