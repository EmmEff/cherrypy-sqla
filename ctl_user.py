import cherrypy
from databaseSession import DatabaseSession

from databaseManager import dbm
from user_db_api import get_all_users
from user_schema import UserSchema


class UsersController:
    @cherrypy.tools.json_out()
    def get_all_users(self):
        with DatabaseSession(dbm) as my_session:
            users = get_all_users(my_session)

            return UserSchema().dump(users, many=True).data
