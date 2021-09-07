from typing import Dict, List

from marshmallow import Schema, fields


class SingleReportSchema(Schema):
    histogram: List[str] = fields.List(fields.String())
    plot: List[str] = fields.List(fields.String())
    boxplot: List[str] = fields.List(fields.String())
    scatter: List[str] = fields.List(fields.String())
    multi_boxplot: List[str] = fields.List(fields.String())
    multi_plot: List[str] = fields.List(fields.String())
    statistics: bool = fields.Boolean()
    x: List[str] = fields.List(fields.String(required=True))
    y: List[str] = fields.List(fields.String())
