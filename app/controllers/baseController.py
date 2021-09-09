from typing import Dict, List, Type

from flask import Response, request
from marshmallow import Schema

from app.config.configGraphics import Graphics, NonGraphics
from app.contextManager.path.files import PathFiles
from app.exceptions.handler import HandlerError
from app.exceptions.InvalidGraphic import InvalidGraphic
from app.graphics.graphics import GraphicName
from app.messages.returnMessages import MessageReturn
from app.spark.sparkDF import SparkDF


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: None

    def are_create_graphics(self, result_graph: List) -> bool:
        for result in result_graph:
            if not result:
                return False
        return True

    def get_graphics(self, data: Dict) -> List[str]:
        graphic_allow = Graphics.Graphics_Allow
        list_graphics = []
        if graphics := data.get("Graphics"):
            list_graphics = [graphic for graphic in graphics if graphic in graphic_allow]
        return list_graphics

    def create_graphics(
        self, paths: List[str], data: Dict, graphics: List[str]
    ) -> List[bool]:
        results = []
        stock_graphic = GraphicName()
        x_axis = data.get(NonGraphics.X_Axis)
        y_axis = data.get(NonGraphics.Y_Axis)

        for path, graphic in zip(paths, graphics):
            results.append(stock_graphic.create_graphic(graphic, path, x_axis, y_axis))
        return results

    def send_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)

        keys = list(self.data_json.keys())
        types_graphics = self.get_graphics(self.data_json)
        spark = SparkDF()
        columns = spark.get_columns(keys)
        with PathFiles(type_file="pdf") as path_pdf, PathFiles(
            n_paths=len(types_graphics), type_file="png"
        ) as path_img:
            data = spark.get_spark_record(columns, self.data_json)
            results = self.create_graphics(path_img.paths, data, types_graphics)
            if self.are_create_graphics(results):
                self.report().create_report(
                    data[NonGraphics.X_Axis],
                    path_pdf.paths[0],
                    path_img.paths,
                    data.get(NonGraphics.Statistics),
                )

                return MessageReturn().return_file(path_pdf.dir, path_pdf.names[0])

        return HandlerError.handler_middleware_error(InvalidGraphic())
