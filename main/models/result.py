from main.extensions import db
from main.models.timestamp_mixin import TimestampMixin


class ResultModel(db.Model, TimestampMixin):
    """The result model"""

    __tablename__ = 'result'
    id = db.Column(db.Integer(), primary_key=True)
    mode = db.Column(db.String(16))
    time = db.Column(db.SmallInteger())
    accuracy = db.Column(db.Float())
    wpm = db.Column(db.Float())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, mode, time, accuracy, wpm, user_id):
        self.mode = mode
        self.time = time
        self.accuracy = accuracy
        self.wpm = wpm
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
