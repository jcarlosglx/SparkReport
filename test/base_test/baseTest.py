from pathlib import Path

from test.config.configTest import ConfigTest
from typing import Type, NoReturn

from flask import Flask
from flask import Response as FlaskResponse
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema
from uuid import uuid4
from app.schemas.stockSchema import stock_schema

from app.messages.statusMessages import STATUS_200


class BaseGetGeneralTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    path_files: str = f"{Path(__file__).resolve().parent.parent}/files/"
    response_key: str = ConfigTest.response_key
    schema_general_get: Type[Schema]
    header_cvs = list(stock_schema.fieldNames())
    save_file: bool = False

    def save_response_file(self, response: FlaskResponse, type_file: str = "pdf"):
        with open(f"{self.path_files}{uuid4()}.{type_file}", "wb") as archive:
            archive.write(response.data)

    def print_error(self, code: str) -> NoReturn:
        print(f"Expected {self.expect_status_get} got {code}")
        print(f"Expected type {type(self.expect_status_get)} got {type(code)}")

    def test_statistics(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "statistics": True
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

    def test_histogram(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
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

    def test_boxplot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
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

    def test_multi_boxplot_one_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
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

    def test_multi_boxplot_two_x(self, get_app: Flask, get_db: Type[SQLAlchemy]):
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

    def test_plot(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "y": [self.header_cvs[2]],
            "plot": [self.header_cvs[2]]
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

    def test_multi_plot_one_y(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "y": [self.header_cvs[2]],
            "multi_plot": [self.header_cvs[2]]
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

    def test_multi_plot_two_y(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[0]],
            "y": [self.header_cvs[1], self.header_cvs[2]],
            "multi_plot": [self.header_cvs[2]]
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

    def test_scatter(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = {
            "x": [self.header_cvs[1]],
            "y": [self.header_cvs[2]],
            "scatter": [self.header_cvs[2]]
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
