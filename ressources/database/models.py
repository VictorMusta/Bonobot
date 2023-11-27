import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: uuid = Column(Integer, primary_key=True, default=uuid.uuid4())


class Animal(Base):
    __tablename__ = "animal"
    id: uuid.uuid4() = Column(Integer, primary_key=True, default=uuid.uuid4())
    name: str = Column(String(50))
    experience: int = Column(Integer)
    level: int = Column(Integer)
