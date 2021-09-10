from typing import List

from marshmallow import Schema, fields

from app.schemas.validatorSchemas import validate_graphics_name, validate_non_graphics_name


class SingleReportSchema(Schema):

    Graphics: List[str] = fields.List(fields.String(), validate=validate_graphics_name)
    NonGraphics: List[str] = fields.List(fields.String(), validate=validate_non_graphics_name)
    x: List[str] = fields.List(fields.String(required=True))
    y: List[str] = fields.List(fields.String())
