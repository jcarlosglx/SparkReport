from app.controllers.baseController import BaseController
from app.schemas.singleReporteSchema import SingleReportSchema
from app.reports.singleReport import SingleReport


class SingleReportController(BaseController):
    schema = SingleReportSchema
    report = SingleReport
