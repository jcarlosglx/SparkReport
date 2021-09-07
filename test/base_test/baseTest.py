import requests

from test.config.configTest import ConfigTest
from typing import Type, NoReturn

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema
from uuid import uuid4
from requests.models import Response
from app.schemas.stockSchema import stock_schema

from app.messages.statusMessages import STATUS_200


class BaseGetGeneralTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    response_key: str = ConfigTest.response_key
    schema_general_get: Type[Schema]
    header_cvs = list(stock_schema.fieldNames())
    save_file: bool = False

    def save_file(self, response: Response):
        with open(f"{uuid4()}.pdf", "wb") as archive:
            archive.write(response.content)

    def print_error(self, code: str) -> NoReturn:
        print(f"Expected {self.expect_status_get} got {code}")
        print(f"Expected type {type(self.expect_status_get)} got {type(code)}")

    def test_histogram(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": self.header_cvs[1],
            "statistics": True
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        code_response = response.get_json()[self.response_key]
        assert (
                code_response == self.expect_status_get
        ), self.print_error(code_response)

