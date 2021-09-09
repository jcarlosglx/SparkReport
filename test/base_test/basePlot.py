from test.base_test.baseGetTest import BaseGetGeneralTest
from test.base_test.baseGraphicTwoDimensionTest import \
    BaseGraphicTwoDimensionTest
from typing import List, Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseGetPlotTest(BaseGetGeneralTest, BaseGraphicTwoDimensionTest):
    Graphics: List[str] = ["Plot"]

    def test_get_plot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        self.reload_json()
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=self.JSON
        )
        self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)


class BaseGetMultiPlotTest(BaseGetGeneralTest, BaseGraphicTwoDimensionTest):
    Graphics: List[str] = ["MultiPlot"]

    def test_get_multi_plot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        self.reload_json()
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=self.JSON
        )
        self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
