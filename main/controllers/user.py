from flask import jsonify
from werkzeug.exceptions import BadRequest, Unauthorized

from main.app import app
from main.models.user import UserModel
from main.schemas.user import UserSchema
from main.security import encode_jwt
from main.extensions import hashing
from main.helpers import load_request_data


@app.route('/register', methods=['POST'])
@load_request_data(UserSchema)
def register(data):
    """A new user sends username & password to register."""

    # check if username exists
    if UserModel.query.filter_by(username=data['username']).first():
        raise BadRequest('Username existed.')

    # save user's data & response a successful message
    user = UserModel(**data)
    user.save_to_db()
    return jsonify(message='Successfully registered.'), 201


@app.route('/login', methods=['POST'])
@load_request_data(UserSchema)
def login(data):
    """User sends username & password to login.
    :return: successful message & JWT
    """

    # find users from database
    user = UserModel.query.filter_by(
        username=data['username'],
        password=hashing.hash_value(data['password'])
    ).first()

    if user is None:
        raise Unauthorized('Wrong username or password.')

    # generate jwt & response to client
    return jsonify(message='Successfully logged in.',
                   access_token=encode_jwt(user.id),
                   token_type='Bearer'), 200
