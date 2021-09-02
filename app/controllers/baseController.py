from typing import Dict, List, Type

from flask import Response, request
from marshmallow import Schema

from app.config.configDB import DBConfig
from app.config.configGraphics import NamesGraphics
from app.contextManager.path.files import PathFiles
from app.contextManager.spark.sparkDF import SparkDataFrame
from app.exceptions.handler import HandlerError
from app.exceptions.InvalidGraphic import InvalidGraphic
from app.graphics.stockGraphics import StockGraphics
from app.messages.returnMessages import MessageReturn
from app.reports.baseReport import BaseReport
from app.schemas.stockSchema import stock_schema


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: BaseReport

    def are_create_graphics(self, result_graph: List) -> bool:
        for result in result_graph:
            if not result:
                return False
        return True

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
            has_x = NamesGraphics.X_Axis in types_graphics
            has_y = NamesGraphics.Y_Axis in types_graphics
            has_statistics = NamesGraphics.Statistics in types_graphics
            if has_x:
                dict_data[NamesGraphics.X_Axis] = file_df.select(
                    self.data_json[NamesGraphics.X_Axis]
                ).toPandas()
            if has_y:
                dict_data[NamesGraphics.Y_Axis] = file_df.select(
                    self.data_json[NamesGraphics.Y_Axis]
                ).toPandas()
            if has_statistics:
                dict_data[NamesGraphics.Statistics] = StockGraphics().statistics(
                    dict_data[NamesGraphics.Y_Axis]
                )
        return dict_data

    def create_graphics(self, paths: List[str], data: Dict) -> List[bool]:
        results = []
        stock_graphic = StockGraphics()
        x_axis = data.get(NamesGraphics.X_Axis)
        y_axis = data.get(NamesGraphics.Y_Axis)
        if x_axis:
            data.pop(NamesGraphics.X_Axis)
        if y_axis:
            data.pop(NamesGraphics.Y_Axis)
        for i, graphic in enumerate(paths):
            results.append(
                stock_graphic.create_graphic(graphic, paths[i], x_axis, y_axis)
            )
        return results

    def send_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        types_graphics = list(self.data_json.keys())
        with PathFiles(len(types_graphics)) as path_files:
            data = self.get_spark_record(types_graphics)
            results = self.create_graphics(path_files.paths, data)
            if self.are_create_graphics(results):
                with PathFiles() as path_pdf:
                    self.report.create_report(
                        data[NamesGraphics.Y_Axis],
                        path_pdf.paths[0],
                        path_files.paths,
                        data[NamesGraphics.Statistics],
                    )
                    return MessageReturn().return_message()
                    # return MessageReturn().return_file(path_pdf.paths[0], path_files.names[0])

        return HandlerError.handler_middleware_error(InvalidGraphic())
