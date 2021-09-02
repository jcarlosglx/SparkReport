from test.config.configTest import ConfigTest
from test.helpers.dummy_json_test.dummy_json_test import get_dummy_json_test
from typing import Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema

from app.messages.statusMessages import STATUS_200


class BaseGetGeneralTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    response_key: str = ConfigTest.response_key
    schema_general_get: Type[Schema]

    def test_get_general(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = get_dummy_json_test(self.schema_general_get)
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        code_response = response.get_json()[self.response_key]
        assert (
            code_response == self.expect_status_get
        ), f"Expected {self.expect_status_get} got {code_response}"
