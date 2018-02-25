from typing import NoReturn
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    """
    SQLAlchemy 'users' table schema
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name: str = None) -> NoReturn:
        self.name = name
