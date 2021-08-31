from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.singleReportController import SingleReportController

single_report_blueprint = Blueprint("single_report", __name__)
endpoint = EndpointConfig.endpoint_single


@single_report_blueprint.route(f"{endpoint}", methods=["GET"])
def send_report() -> Response:
    return SingleReportController().send_report()
