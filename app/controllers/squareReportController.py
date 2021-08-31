from app.controllers.baseController import BaseController
from app.schemas.squareReporteSchema import SquareReportSchema
from app.reports.squareReport import SquareReport


class SquareReportController(BaseController):
    schema = SquareReportSchema
    report = SquareReport
