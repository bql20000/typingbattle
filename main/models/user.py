from main.extensions import db, hashing
from main.models.timestamp_mixin import TimestampMixin


class UserModel(db.Model, TimestampMixin):
    """The user model"""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.CHAR(64))       # length of SHA-256 hash value

    results = db.relationship('ResultModel')

    def __init__(self, username, password):
        self.username = username
        self.password = hashing.hash_value(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
