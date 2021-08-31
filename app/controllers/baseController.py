
from flask import Response, request
from app.contextManager.spark.sparkDF import SparkDataFrame
from app.contextManager.path.files import PathFiles
from app.exceptions.handler import HandlerError
from app.messages.returnMessages import MessageReturn
from typing import Type, List, Dict
from app.exceptions.InvalidData import InvalidData
from app.graphics.stockGraphics import StockGraphics
from app.exceptions.InvalidGraphic import InvalidGraphic
from marshmallow import Schema
from app.config.configGraphics import TypesGraphics
from app.schemas.stockSchema import stock_schema
from app.config.configDB import DBConfig
from app.reports.baseReport import BaseReport
from pandas import DataFrame


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
            has_x = "x" in types_graphics
            has_y = "y" in types_graphics
            has_statistics = "statistics" in types_graphics
            if has_x:
                dict_data["x"] = file_df.select(self.data_json["x"]).toPandas()
            if has_y:
                dict_data["y"] = file_df.select(self.data_json["y"]).toPandas()
            if has_statistics:
                dict_data["statistics"] = True
        return dict_data

    def create_graphics(self, paths: List[str], data: Dict[str]) -> List[bool]:
        results = []
        stock_graphic = StockGraphics()
        keys = data.keys()
        for i, graphic in enumerate(paths):
            if "x" in keys:
                method = getattr(stock_graphic, graphic)
                results.append(method(data["y"], paths[i]))
            elif ("x" in keys) and ("y" in keys):
                method = getattr(stock_graphic, graphic)
                results.append(method(data["x"], data["y"], paths[i]))
        return results

    def get_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        types_graphics = self.data_json.keys()
        with PathFiles(len(types_graphics)) as paths:
            data = self.get_spark_record(types_graphics)
            keys = data.keys()
            results = self.create_graphics(paths, data)
            if "statistics" in keys:
                other_data = StockGraphics().statistics(data["y"])
            if self.are_create_graphics(results):
                self.report.create_report(data["y"], "single.pdf", paths, other_data)
                return MessageReturn().access_record_message("")
        return HandlerError.handler_middleware_error(InvalidGraphic())

