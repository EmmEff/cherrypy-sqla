#!/usr/bin/env python

import cherrypy
import ctl_user
from util import jsonify_error


def main():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    ctl_user.map_controller(dispatcher)

    config = {
        '/': {
            'request.dispatch': dispatcher,
            'error_page.default': jsonify_error,
        }
    }

    cherrypy.tree.mount(root=None, config=config)

    cherrypy.engine.start()

    cherrypy.engine.block()


if __name__ == '__main__':
    main()