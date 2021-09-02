from werkzeug.exceptions import HTTPException

from app.messages.errorMessages import ERROR_MSG_INVALID_GRAPHIC
from app.messages.statusMessages import STATUS_424


class InvalidGraphic(HTTPException):
    code = int(STATUS_424)
    description = ERROR_MSG_INVALID_GRAPHIC
