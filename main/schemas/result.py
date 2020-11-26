from marshmallow import Schema, fields


class ResultSchema(Schema):
    mode = fields.Str(required=True)
    time = fields.Int(required=True)
    accuracy = fields.Float(required=True)
    wpm = fields.Float(required=True)
    created = fields.Str()
    updated = fields.Str(dump_only=True)
