from main.extensions import db


class ProductModel(db.Model):
    """The product model."""
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    thumbnail = db.Column(db.String(128))
    rating = db.Column(db.Float())
    total_reviews = db.Column(db.Integer())
    url = db.Column(db.String(128))
    currency = db.Column(db.String(16))
    price = db.Column(db.Float())

    def __init__(self, title, thumbnail, rating, url, price, currency, total_reviews):
        self.title = title
        self.thumbnail = thumbnail
        self.rating = rating
        self.total_reviews = total_reviews
        self.url = url
        self.price = price
        self.currency = currency


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
