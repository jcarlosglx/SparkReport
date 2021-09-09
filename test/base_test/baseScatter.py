from test.base_test.baseTest import BaseGetGeneralTest
from typing import List, Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseGetScatterTest(BaseGetGeneralTest):
    X_Axis: str = BaseGetGeneralTest.header_cvs[1]
    Y_Axis: List[str] = [BaseGetGeneralTest.header_cvs[2]]

    def test_get_scatter(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": self.X_Axis,
            "y": self.Y_Axis,
            "Graphics": ["Scatter"],
        }
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        if self.save_file:
            self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
