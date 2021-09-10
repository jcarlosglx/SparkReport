from test.base_test.base_http.baseGetTest import BaseGetGeneralTest
from test.base_test.base_dimension.baseGraphicTwoDimensionTest import \
    BaseGraphicTwoDimensionTest
from typing import Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config.configEndpoint import EndpointConfig
from app.messages.statusMessages import STATUS_200


class BaseMultiGraphicsTwoDimension(BaseGetGeneralTest, BaseGraphicTwoDimensionTest):
    Graphics = BaseGraphicTwoDimensionTest.TypeGraphics[:]
    endpoint_get = EndpointConfig.endpoint_square
    expect_status_get = STATUS_200

    def test(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        self.reload_json()
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=self.JSON
        )
        self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
