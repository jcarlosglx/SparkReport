from test.base_test.baseTest import BaseGetGeneralTest
from typing import List, Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseGetBoxPlotTest(BaseGetGeneralTest):
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Graphics: List[str] = ["BoxPlot"]

    def test_get_boxplot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {"x": self.X_Axis, "Graphics": self.Graphics}
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)


class BaseGetMultiBoxPlotTest(BaseGetGeneralTest):

    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    X_N_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1], BaseGetGeneralTest.header_cvs[2]]
    Graphics: List[str] = ["MultiBoxPlot"]

    def test_get_multi_boxplot_one_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {"x": self.X_Axis, "Graphics": self.Graphics}
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)

    def test_get_multi_boxplot_multi_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {"x": self.X_N_Axis, "Graphics": ["MultiBoxPlot"]}
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
