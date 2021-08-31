from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.quarterReportController import QuarterReportController

quarter_report_blueprint = Blueprint("quarter_report", __name__)
endpoint = EndpointConfig.endpoint_quarter


@quarter_report_blueprint.route(f"{endpoint}", methods=["GET"])
def send_report() -> Response:
    return QuarterReportController().send_report()
