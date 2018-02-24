from tbl_user import User


def get_all_users(session):
    return session.query(User).all()
