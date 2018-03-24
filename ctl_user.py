from typing import List, NoReturn
import cherrypy
from databaseSession import DatabaseSession

from databaseManager import dbm
from user_db_api import get_all_users, get_user_by_id, add_user
from user_schema import UserSchema


class UsersController:
    """
    CherryPy handler for "/users" URL
    """
    @cherrypy.tools.json_out()
    def get_all_users(self, **kwargs) -> List[dict]:
        with DatabaseSession(dbm) as my_session:
            if 'filter' in kwargs:
                users = []
            else:
                users = get_all_users(my_session)

            return UserSchema().dump(users, many=True).data

    @cherrypy.tools.json_out()
    def get_user(self, user_id) -> dict:
        with DatabaseSession(dbm) as my_session:
            user = get_user_by_id(my_session, user_id)
            if not user:
                raise cherrypy.HTTPError(404, f'User [{user_id}] not found')

            return UserSchema().dump(user).data

    @cherrypy.tools.json_in()
    def add_user(self):
        with DatabaseSession(dbm) as my_session:
            # validate add user POST data
            data, errors = UserSchema().load(cherrypy.request.json)

            if errors:
                raise cherrypy.HTTPError(
                    400, 'Malformed POST data: {}'.format(['\n'.join(errors)]))

            add_user(my_session, data)

            my_session.commit()

            cherrypy.response.status = 201

            return ''


def map_controller(dispatcher) -> NoReturn:
    users_controller = UsersController()

    dispatcher.connect(name='users',
                       route='/users',
                       action='get_all_users',
                       controller=users_controller,
                       conditions={'method': ['GET']})

    dispatcher.connect(name='get_user',
                       route='/users/:(user_id)',
                       action='get_user',
                       controller=users_controller,
                       conditions={'method': ['GET']})

    dispatcher.connect(name='add_user',
                       route='/users',
                       action='add_user',
                       controller=users_controller,
                       conditions={'method': ['POST']})
