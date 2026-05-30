from marshmallow import Schema, fields


class OfferSchema(Schema):
    id = fields.Str(dump_only=True)
    itemName = fields.Str(required=True)
    message = fields.Str(required=True)
    lender = fields.Str(required=True)
    type = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)
