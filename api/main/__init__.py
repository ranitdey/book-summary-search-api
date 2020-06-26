from flask import Flask
from .controller import api
from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    api.init_app(app)
    app.config.from_object(config_by_name[config_name])
    return app

