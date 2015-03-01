from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder=None)
    default_config = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'utils/config.py')
    app.config.from_pyfile(default_config)

    from elric import models

    db.init_app(app)

    from elric.endpoints import ENDPOINTS

    api = Api(app)

    for urlclass, url in ENDPOINTS:
        api.add_resource(urlclass, url)
    return app