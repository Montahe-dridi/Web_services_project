from marshmallow import Schema, fields

class RideSchema(Schema):
    id = fields.Str(dump_only=True)
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)
    datetime = fields.DateTime(required=True)
    seats_available = fields.Int(required=True)
    user_id = fields.Str(required=True)