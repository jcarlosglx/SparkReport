from app.controllers.baseController import BaseController
from app.schemas.squareReporteSchema import SquareReportSchema


class SquareReportController(BaseController):
    schema = SquareReportSchema
