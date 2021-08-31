
from flask import Response, request
from app.contextManager.spark.sparkDF import SparkDataFrame
from app.contextManager.path.files import PathFiles
from app.exceptions.handler import HandlerError
from app.messages.returnMessages import MessageReturn
from typing import Type, List, Dict
from app.graphics.stockGraphics import StockGraphics
from app.exceptions.InvalidGraphic import InvalidGraphic
from marshmallow import Schema
from app.config.configGraphics import NamesGraphics
from app.schemas.stockSchema import stock_schema
from app.config.configDB import DBConfig
from app.reports.baseReport import BaseReport


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: BaseReport

    def are_create_graphics(self, result_graph: List[bool]) -> bool:
        for result in result_graph:
            if not result:
                return False
        return True

    def get_spark_record(self, types_graphics: List[str]) -> Dict[str]:
        with SparkDataFrame() as spark_df:
            dict_data = {}
            file_df = spark_df.spark_session.read \
                .format("csv") \
                .option("header", True).option("delimiter", ",") \
                .schema(stock_schema) \
                .load(DBConfig.STOCK_DB)
            has_x = NamesGraphics.X_Axis in types_graphics
            has_y = NamesGraphics.Y_Axis in types_graphics
            has_statistics = NamesGraphics.Statistics in types_graphics
            if has_x:
                dict_data[NamesGraphics.X_Axis] = file_df.select(self.data_json[NamesGraphics.X_Axis]).toPandas()
            if has_y:
                dict_data[NamesGraphics.Y_Axis] = file_df.select(self.data_json[NamesGraphics.Y_Axis]).toPandas()
            if has_statistics:
                dict_data[NamesGraphics.Statistics] = StockGraphics().statistics(dict_data[NamesGraphics.Y_Axis])
        return dict_data

    def create_graphics(self, paths: List[str], data: Dict[str]) -> List[bool]:
        results = []
        stock_graphic = StockGraphics()
        keys = data.keys()
        for i, graphic in enumerate(paths):
            if NamesGraphics.X_Axis in keys:
                method = getattr(stock_graphic, graphic)
                results.append(method(data[NamesGraphics.Y_Axis], paths[i]))
            elif (NamesGraphics.X_Axis in keys) and (NamesGraphics.Y_Axis in keys):
                method = getattr(stock_graphic, graphic)
                results.append(method(data[NamesGraphics.X_Axis], data[NamesGraphics.Y_Axis], paths[i]))
        return results

    def send_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        types_graphics = self.data_json.keys()
        with PathFiles(len(types_graphics)) as img_paths:
            data = self.get_spark_record(types_graphics)
            results = self.create_graphics(img_paths, data)
            if self.are_create_graphics(results):
                with PathFiles() as path_pdf:
                    self.report.create_report(data[NamesGraphics.Y_Axis], path_pdf[0], img_paths, data[NamesGraphics.Statistics])
                    return MessageReturn().access_record_message("")

        return HandlerError.handler_middleware_error(InvalidGraphic())

