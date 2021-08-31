from app.controllers.baseController import BaseController
from app.schemas.singleReporteSchema import SingleReportSchema


class SingleReportController(BaseController):
    schema = SingleReportSchema
