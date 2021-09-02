from werkzeug.exceptions import HTTPException

from app.messages.errorMessages import ERROR_MSG_INVALID_DATA
from app.messages.statusMessages import STATUS_424


class InvalidData(HTTPException):
    code = int(STATUS_424)
    description = ERROR_MSG_INVALID_DATA
