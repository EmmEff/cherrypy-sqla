from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from database import Base
import tbl_user  # noqa pylint: disable=unused-import


class DatabaseManager:
    """
    Pseudo database manager for SQLAlchemy
    """
    def __init__(self, engine=None):
        if not engine:
            my_engine = create_engine('sqlite:///mydb.sqlite', echo=False)

            Base.metadata.create_all(my_engine)

            self.engine = my_engine
        else:
            self.engine = engine

        session_factory = sessionmaker(bind=self.engine)

        self.session_cls = scoped_session(session_factory)

    def open_session(self):
        return self.session_cls()

    def close_session(self):
        self.session_cls.remove()


dbm = DatabaseManager()
