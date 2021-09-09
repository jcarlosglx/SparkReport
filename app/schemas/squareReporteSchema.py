from app.schemas.validatorSchemas import validate_graphics_name
from typing import Dict, List

from marshmallow import Schema, fields


class SquareReportSchema(Schema):
    Graphics: List[str] = fields.List(fields.String(), validate=validate_graphics_name)
    Statistics: bool = fields.Boolean()
    x: List[str] = fields.List(fields.String(required=True))
    y: List[str] = fields.List(fields.String())
