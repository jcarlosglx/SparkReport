from app.controllers.baseController import BaseController
from app.models.logModel import LogModel


class LogsController(BaseController):
    model = LogModel
