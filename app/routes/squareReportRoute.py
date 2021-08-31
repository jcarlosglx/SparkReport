from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.squareReportController import SquareReportController

square_report_blueprint = Blueprint("square_report", __name__)
endpoint = EndpointConfig.endpoint_square


@square_report_blueprint.route(f"{endpoint}", methods=["GET"])
def send_report() -> Response:
    return SquareReportController().send_report()
