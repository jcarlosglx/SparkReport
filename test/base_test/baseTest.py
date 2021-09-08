from pathlib import Path

from test.config.configTest import ConfigTest
from typing import Type, NoReturn

from flask import Response as FlaskResponse
from marshmallow import Schema
from uuid import uuid4
from app.schemas.stockSchema import stock_schema

from app.messages.statusMessages import STATUS_200


class BaseGetGeneralTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    path_files: str = f"{Path(__file__).resolve().parent.parent}/files/"
    response_key: str = ConfigTest.response_key
    header_cvs = list(stock_schema.fieldNames())
    save_file: bool = False

    def save_response_file(self, response: FlaskResponse, type_file: str = "pdf"):
        with open(f"{self.path_files}{uuid4()}.{type_file}", "wb") as archive:
            archive.write(response.data)

    def print_error(self, code: str) -> NoReturn:
        print(f"Expected {self.expect_status_get} got {code}")
        print(f"Expected type {type(self.expect_status_get)} got {type(code)}")


