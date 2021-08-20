from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.LogsController import LogsController

logs_blueprint = Blueprint("logs", __name__)
endpoint = EndpointConfig.endpoint_logs


@logs_blueprint.route(f"{endpoint}", methods=["GET"])
def get_logs() -> Response:
    return LogsController().get_all_records()


@logs_blueprint.route(f"{endpoint}/<id_record>", methods=["GET"])
def get_log(id_record) -> Response:
    return LogsController().get_individual_record(id_record)
