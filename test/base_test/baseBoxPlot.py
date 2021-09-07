from test.base_test.baseTest import BaseGetGeneralTest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Type


class BaseGetBoxPlotTest(BaseGetGeneralTest):
    def test_get_boxplot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "boxplot": [self.header_cvs[2]]
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert (
                code_response == self.expect_status_get
        ), self.print_error(code_response)


class BaseGetMultiBoxPlotTest(BaseGetGeneralTest):
    def test_get_multi_boxplot_one_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "multi_boxplot": [self.header_cvs[2]]
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert (
                code_response == self.expect_status_get
        ), self.print_error(code_response)

    def test_get_multi_boxplot_two_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1], self.header_cvs[2]],
            "multi_boxplot": [self.header_cvs[2]]
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert (
                code_response == self.expect_status_get
        ), self.print_error(code_response)

