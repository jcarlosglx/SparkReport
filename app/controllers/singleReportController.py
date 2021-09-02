from app.controllers.baseController import BaseController
from app.reports.singleReport import SingleReport
from app.schemas.singleReporteSchema import SingleReportSchema


class SingleReportController(BaseController):
    schema = SingleReportSchema
    report = SingleReport
