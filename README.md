Advanced CherryPy + SQLAlchemy example
======================================

In this example, the [CherryPy](https://cherrypy.org)-based REST API server
uses [SQLAlchemy](https://sqlalchemy.org) as the ORM with a backing SQLite
database for the backend.

Usage
-----

The "entry point" for this example is `server.py`. Create a `virtualenv` and
run `server.py` to launch the REST API server. By default, it listens only on
`localhost` on port `8080`.

```shell
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 server.py
```

Alternatively, for `pipenv` users:

```shell
pipenv install
python3 server.py
```

The SQLite3 database is named `mydb.sqlite`. It is automatically created in
current directory (wherever `server.py` is executed).

Details
-------

[Marshmallow](https://marshmallow.readthedocs.io) is used to serialize the
SQLAlchemy results objects and deserialize the POST data on the create
requests.
