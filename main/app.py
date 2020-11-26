import logging

from flask import Flask, jsonify
from flask_cors import CORS
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from main.extensions import db, hashing


def create_app():
    app = Flask(__name__)
    CORS(app)
    try:
        app.config.from_object(f'config.{app.config["ENV"]}.config')
    except:
        raise Exception(f'Unknown environment {app.config["ENV"]}.')
    return app


def register_controllers():
    import main.controllers
    import main.models


def register_extensions():
    """Register the application with needed extensions."""
    hashing.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()


app = create_app()
register_controllers()
register_extensions()


@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all application's exceptions."""
    if isinstance(e, ValidationError):
        logging.exception(e)
        return jsonify(message='Invalid request data.', error_info=e.messages), 400

    if isinstance(e, HTTPException):
        logging.exception(e)
        return jsonify(message=e.description,
                       error_info=e.response.data if e.response else {}
                       ), e.code

    logging.exception(e)
    return jsonify(message='Internal server error.', error_info={}), 500

