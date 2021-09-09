from test.base_test.baseTest import BaseGetGeneralTest
from typing import List, Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseGetPlotTest(BaseGetGeneralTest):
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[0]]
    Y_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Graphics: List[str] = ["Plot"]

    def test_get_plot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {"x": self.X_Axis, "y": self.Y_Axis, "Graphics": self.Graphics}
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)


class BaseGetMultiPlotTest(BaseGetGeneralTest):
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[0]]
    Y_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Y_N_Axis = [BaseGetGeneralTest.header_cvs[1], BaseGetGeneralTest.header_cvs[2]]
    Graphics: List[str] = ["MultiPlot"]

    def test_get_multi_plot_one_y(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": self.X_Axis,
            "y": self.Y_Axis,
            "Graphics": self.Graphics,
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)

    def test_get_multi_plot_two_y(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": self.X_Axis,
            "y": self.Y_N_Axis,
            "Graphics": self.Graphics,
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
