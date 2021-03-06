from test.base_test.base_http.baseGetTest import BaseGetGeneralTest
from typing import List, Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class BaseGetStatisticsTest(BaseGetGeneralTest):
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]

    def test_get_statistics(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {"x": self.X_Axis, "NonGraphics": ["Statistics"]}
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}", json=json_data
        )
        self.save_response_file(response)
        code_response = str(response.status_code)
        assert code_response == self.expect_status_get, self.print_error(code_response)
