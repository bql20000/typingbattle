import os
import logging

from flask import Flask, jsonify
from flask_cors import CORS
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from main.extensions import db, hashing


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(f'config.{os.getenv("ENVIRONMENT")}.config')
    return app


def register_subpackages():
    import main.controllers
    import main.models


def register_extensions():
    """Register the application with needed extensions."""
    logging.basicConfig(
        filename=app.config['LOGGING_FILE'],
        format='%(asctime)s %(levelname)-5s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=app.config['LOGGING_LEVEL'],
    )
    hashing.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()


app = create_app()
register_subpackages()
register_extensions()


@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all application's exceptions."""

    if isinstance(e, ValidationError):
        return jsonify(message='Invalid request data.', error_info=e.messages), 400

    if isinstance(e, HTTPException):
        return jsonify(message=e.description,
                       error_info=e.response.data if e.response else {}
                       ), e.code

    logging.exception(e)
    return jsonify(message='Internal server error.', error_info={}), 500


# This is to prevent browser from caching APIs response since
# it might cause some weird bugs if the browser did
@app.after_request
def prevent_browser_caching(response):
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Pragma'] = 'no-cache'
    return response
