import os

import pytest

from main.extensions import db
from main.app import app
from tests.helpers import create_db_samples


env = os.getenv("ENVIRONMENT")
if env != 'test':
    print('Tests should be run in test environment')
    exit(1)


def reset_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_db_samples()


@pytest.fixture
def client():
    reset_db()
    return app.test_client()
