from marshmallow import Schema, fields, validate


class BorrowRequestSchema(Schema):
    id = fields.Str(dump_only=True)
    itemName = fields.Str(required=True)
    message = fields.Str(required=True)
    time = fields.Int(required=True, validate=validate.Range(min=0))
    borrower = fields.Str(required=True)
    type = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)
