from marshmallow import Schema, fields


class ProductSchema(Schema):
    title = fields.Str(required=True)
    thumbnail = fields.Str(required=True)
    url = fields.Str(required=True)
    currency = fields.Str(required=True)
    price = fields.Float(required=True)
    rating = fields.Float(required=True)
    total_reviews = fields.Int(required=True)

