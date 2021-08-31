from app.controllers.baseController import BaseController
from app.schemas.quarterReporteSchema import QuarterReportSchema
from app.reports.quarterReport import QuarterReport


class QuarterReportController(BaseController):
    schema = QuarterReportSchema
    report = QuarterReport
