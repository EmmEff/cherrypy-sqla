class DatabaseSession:
    """
    Context manager to handle SQLAlchemy session
    """
    def __init__(self, dbm):
        self.dbm = dbm
        self.session = None

    def __enter__(self):
        self.session = self.dbm.open_session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.rollback()

        self.dbm.close_session()
