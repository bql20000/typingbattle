from flask import Flask, render_template
from flask_cors import CORS

from main.extensions import db


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


def register_extensions():
    db.init_app(app)


app = create_app()
register_controllers()
register_extensions()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
