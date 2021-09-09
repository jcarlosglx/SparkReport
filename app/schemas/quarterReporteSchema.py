from typing import List

from marshmallow import Schema, fields
from app.schemas.validatorSchemas import validate_graphics_name


class QuarterReportSchema(Schema):
    Graphics: List[str] = fields.List(fields.String(), validate=validate_graphics_name)
    Statistics: bool = fields.Boolean()
    x: str = fields.String(required=True)
    y: List[str] = fields.List(fields.String())
