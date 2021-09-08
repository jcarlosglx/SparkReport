from typing import Dict, List

from marshmallow import Schema, fields


class SingleReportSchema(Schema):
    Histogram: List[str] = fields.List(fields.String())
    Plot: List[str] = fields.List(fields.String())
    BoxPlot: List[str] = fields.List(fields.String())
    Scatter: List[str] = fields.List(fields.String())
    MultiBoxPlot: List[str] = fields.List(fields.String())
    MultiPlot: List[str] = fields.List(fields.String())
    Statistics: bool = fields.Boolean()
    x: List[str] = fields.List(fields.String(required=True))
    y: List[str] = fields.List(fields.String())
