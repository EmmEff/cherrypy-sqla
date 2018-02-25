"""
Universal "User" database APIs

All APIs return SQLAlchemy objects
"""

from typing import List, NoReturn
from tbl_user import User


def get_all_users(session) -> List[User]:
    """
    Return all users

    :param session: SQLAlchemy database session object
    :return: list of User objects
    """
    return session.query(User).all()


def get_user_by_id(session, user_id: int) -> User:
    """
    get user by id

    :param session: SQLAlchemy database session object
    :param user_id: id of user
    :return: User object
    """
    return session.query(User).get(user_id)


def add_user(session, user_dict: dict) -> NoReturn:
    user = User(name=user_dict['name'])

    session.add(user)
