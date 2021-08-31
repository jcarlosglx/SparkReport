from marshmallow import Schema, fields
from typing import Dict, List


class QuarterReportSchema(Schema):
    histogram: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.String())
    plot: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.String())
    boxplot: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.String())
    scatter: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.String())
    multi_boxplot: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.List(fields.String()))
    multi_plot: Dict[str, str] = fields.Dict(keys=fields.String(), values=fields.List(fields.String()))
    statistics: bool = fields.Boolean()
    x: str = fields.String(required=True)
    y: List[str] = fields.List(fields.String(), required=True)
