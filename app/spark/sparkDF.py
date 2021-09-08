from app.contextManager.spark.sparkDF import SparkDataFrame
from app.config.configDB import DBConfig
from app.schemas.stockSchema import stock_schema
from typing import List, Dict
from app.graphics.stockGraphics import StockGraphics
from app.config.configGraphics import NonGraphics


class SparkDF:

    def get_columns(self, graphics: List[str]) -> List[str]:
        names = []
        keys = NonGraphics.get_values()
        for graphic in graphics:
            if graphic in keys:
                names.append(graphic)
        return names

    def get_spark_record(self, types_graphics: List[str], data_json: Dict) -> Dict:
        dict_data = {}

        with SparkDataFrame() as spark_df:
            file_df = (
                spark_df.spark_session.read.format("csv")
                    .option("header", True)
                    .option("delimiter", ",")
                    .schema(stock_schema)
                    .load(DBConfig.STOCK_DB)
            )

            if NonGraphics.X_Axis in types_graphics:
                dict_data[NonGraphics.X_Axis] = file_df.select(
                    data_json[NonGraphics.X_Axis]
                ).toPandas()

            if NonGraphics.Y_Axis in types_graphics:
                dict_data[NonGraphics.Y_Axis] = file_df.select(
                    data_json[NonGraphics.Y_Axis]
                ).toPandas()

            if NonGraphics.Statistics in types_graphics:
                dict_data[NonGraphics.Statistics] = StockGraphics().statistics(
                    dict_data[NonGraphics.X_Axis]
                )
        return dict_data
