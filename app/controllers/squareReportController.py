from app.controllers.baseController import BaseController
from app.reports.squareReport import SquareReport
from app.schemas.squareReporteSchema import SquareReportSchema


class SquareReportController(BaseController):
    schema = SquareReportSchema
    report = SquareReport
