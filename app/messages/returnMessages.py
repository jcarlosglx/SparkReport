from flask import Response, jsonify, send_from_directory

from app.messages.statusMessages import STATUS_200
from app.messages.successMessages import SUCCESS_MSG_200, SUCCESS_MSG_GET


class MessageReturn:
    message = SUCCESS_MSG_200
    status = STATUS_200
    data = ""

    def return_message(self) -> Response:
        response = jsonify(data=self.data, status=self.status, message=self.message)
        response._status = self.status
        return response

    def custom_return_message(self, data: str, message: str, status: str) -> Response:
        self.data = data
        self.status = status
        self.message = message
        return self.return_message()

    def access_record_message(self, data) -> Response:
        self.status = STATUS_200
        self.data = data
        self.message = SUCCESS_MSG_GET
        return self.return_message()

    def return_file(self, path: str, name: str) -> Response:
        self.status = STATUS_200
        response = send_from_directory(path, filename=name, as_attachment=True)
        response._status = self.status
        return response
