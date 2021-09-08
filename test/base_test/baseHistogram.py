from test.base_test.baseTest import BaseGetGeneralTest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import Type, List


class BaseGetHistogramTest(BaseGetGeneralTest):
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]

    def test_get_histogram(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": self.X_Axis,
            "histogram": [self.header_cvs[2]]
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
