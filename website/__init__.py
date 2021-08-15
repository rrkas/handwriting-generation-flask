from os import urandom

import flask


class _Config:
    SECRET_KEY = urandom(8)
    UPLOAD_FOLDER = 'static/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


app = flask.Flask(__name__)
app.config.from_object(_Config())

from .routes import *
