from app.controllers.baseController import BaseController
from app.schemas.quarterReporteSchema import QuarterReportSchema


class QuarterReportController(BaseController):
    schema = QuarterReportSchema
