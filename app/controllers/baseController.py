from typing import Dict, List, Type

from flask import Response, request
from marshmallow import Schema

from app.config.configDB import DBConfig
from app.config.configGraphics import NonGraphics, Graphics
from app.contextManager.path.files import PathFiles
from app.contextManager.spark.sparkDF import SparkDataFrame
from app.exceptions.handler import HandlerError
from app.exceptions.InvalidGraphic import InvalidGraphic
from app.graphics.stockGraphics import StockGraphics
from app.messages.returnMessages import MessageReturn
from app.schemas.stockSchema import stock_schema


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: None

    def are_create_graphics(self, result_graph: List) -> bool:
        for result in result_graph:
            if not result:
                return False
        return True

    def get_graphics(self, graphics: List[str]) -> List[str]:
        names = []
        keys = Graphics.get_values()
        for graphic in graphics:
            if graphic in keys:
                names.append(graphic)
        return names

    def get_columns(self, graphics: List[str]) -> List[str]:
        names = []
        keys = NonGraphics.get_values()
        for graphic in graphics:
            if graphic in keys:
                names.append(graphic)
        return names

    def get_spark_record(self, types_graphics: List[str]) -> Dict:
        dict_data = {}
        with SparkDataFrame() as spark_df:
            file_df = (
                spark_df.spark_session.read.format("csv")
                .option("header", True)
                .option("delimiter", ",")
                .schema(stock_schema)
                .load(DBConfig.STOCK_DB)
            )
            has_x = NonGraphics.X_Axis in types_graphics
            has_y = NonGraphics.Y_Axis in types_graphics
            has_statistics = NonGraphics.Statistics in types_graphics
            if has_x:
                dict_data[NonGraphics.X_Axis] = file_df.select(
                    self.data_json[NonGraphics.X_Axis]
                ).toPandas()
            if has_y:
                dict_data[NonGraphics.Y_Axis] = file_df.select(
                    self.data_json[NonGraphics.Y_Axis]
                ).toPandas()
            if has_statistics:
                dict_data[NonGraphics.Statistics] = StockGraphics().statistics(
                    dict_data[NonGraphics.X_Axis]
                )
        return dict_data

    def create_graphics(self, paths: List[str], data: Dict) -> List[bool]:
        results = []
        stock_graphic = StockGraphics()
        keys = data.keys()
        x_axis = None
        y_axis = None
        has_x = NonGraphics.X_Axis in keys
        has_y = NonGraphics.Y_Axis in keys
        if has_x:
            x_axis = data[NonGraphics.X_Axis]
        if has_y:
            y_axis = data[NonGraphics.Y_Axis]

        for i, graphic in enumerate(paths):
            results.append(
                stock_graphic.create_graphic(graphic, paths[i], x_axis, y_axis)
            )
        return results

    def send_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)

        keys = list(self.data_json.keys())
        types_graphics = self.get_graphics(keys)
        columns = self.get_columns(keys)
        with PathFiles(type_file="pdf") as path_pdf, PathFiles(n_paths=len(types_graphics), type_file="png") as path_img:
            data = self.get_spark_record(columns)
            results = self.create_graphics(path_img.paths, data)

            self.report().create_report(
                data[NonGraphics.X_Axis],
                path_pdf.paths[0],
                path_img.paths,
                data[NonGraphics.Statistics],
            )

            if self.are_create_graphics(results):
                return MessageReturn().return_file(path_pdf.dir, path_pdf.names[0])

        return HandlerError.handler_middleware_error(InvalidGraphic())
