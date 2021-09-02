from app.controllers.baseController import BaseController
from app.reports.quarterReport import QuarterReport
from app.schemas.quarterReporteSchema import QuarterReportSchema


class QuarterReportController(BaseController):
    schema = QuarterReportSchema
    report = QuarterReport
