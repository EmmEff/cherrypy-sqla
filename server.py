#!/usr/bin/env python

import cherrypy
from ctl_user import UsersController


def main():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    dispatcher.connect(name='users',
                       route='/users',
                       action='get_all_users',
                       controller=UsersController(),
                       conditions={'method': ['GET']})

    config = {
        '/': {
            'request.dispatch': dispatcher,
        }
    }

    cherrypy.tree.mount(root=None, config=config)

    cherrypy.engine.start()

    cherrypy.engine.block()


if __name__ == '__main__':
    main()