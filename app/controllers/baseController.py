
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


class BaseController:
    data_json = request.get_json()
    schema: Type[Schema]
    report: BaseReport

    def get_report(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        types_graphics = self.data_json.keys()
        with PathFiles(len(types_graphics)) as paths:
            with SparkDataFrame() as spark_df:
                stock_graphic = StockGraphics()
                file_df = spark_df.spark_session.read \
                    .format("csv") \
                    .option("header", True).option("delimiter", ",") \
                    .schema(stock_schema) \
                    .load(DBConfig.STOCK_DB)
                has_x = "x" in types_graphics
                has_y = "y" in types_graphics
                has_statistics = "statistics" in types_graphics
                other_data = None
                if has_x:
                    stock_x_df = file_df.select(self.data_json["x"]).toPandas()
                if has_y:
                    stock_y_df = file_df.select(self.data_json["y"]).toPandas()

                for i, graphic in enumerate(paths):
                    if not has_x:
                        method = getattr(stock_graphic, graphic)
                        method(stock_y_df, paths[i])
                    elif has_x and has_y:
                        method = getattr(stock_graphic, graphic)
                        method(stock_x_df, stock_y_df, paths[i])
                    if has_statistics:
                        other_data = stock_graphic.statistics(stock_y_df)

                self.report.create_report(stock_y_df, "single.pdf", paths, other_data)

                return MessageReturn().access_record_message("")

