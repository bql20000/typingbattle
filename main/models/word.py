from main.extensions import db


class WordModel(db.Model):
    """The word model."""
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(16))

    def __init__(self, value):
        self.value = value

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
