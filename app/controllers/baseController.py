from typing import Dict, List, Type

from flask import Response, request
from marshmallow import Schema
from app.controllers.parserinformation import ParserInformation
from app.config.configGraphics import AxisGraphics, Graphics, NonGraphics
from app.contextManager.path.files import PathFiles
from app.exceptions.handler import HandlerError
from app.exceptions.InvalidGraphic import InvalidGraphic
from app.controllers.creatorinformation import CreatorInformation
from app.messages.returnMessages import MessageReturn
from app.reports.baseReport import BaseReport
from app.spark.sparkDF import SparkDF


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: Type[BaseReport]

    def send_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        parser = ParserInformation()
        types_graphics = parser.get_graphics(self.data_json)
        types_non_graphics = parser.get_non_graphics(self.data_json)
        spark = SparkDF()
        columns = parser.get_axis(self.data_json)
        creator = CreatorInformation()
        with PathFiles(type_file="pdf") as path_pdf, PathFiles(
            n_paths=len(types_graphics), type_file="png"
        ) as path_img:
            data = spark.get_spark_record(columns, self.data_json)
            results = creator.create_graphics(path_img.paths, data, types_graphics)
            if creator.are_create_graphics(results):

                non_graphics = None
                if types_non_graphics:
                    non_graphics = creator.create_non_graphics(self.data_json, types_non_graphics)

                self.report().create_report(
                    data[AxisGraphics.X_Axis],
                    path_pdf.paths[0],
                    path_img.paths,
                    non_graphics,
                    )

                return MessageReturn().return_file(path_pdf.dir, path_pdf.names[0])

        return HandlerError.handler_middleware_error(InvalidGraphic())
