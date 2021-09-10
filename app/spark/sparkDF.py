from typing import Dict, List

from app.config.configDB import DBConfig
from app.config.configGraphics import AxisGraphics
from app.contextManager.spark.sparkDF import SparkDataFrame
from app.schemas.stockSchema import stock_schema


class SparkDF:
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

            if AxisGraphics.X_Axis in types_graphics:
                dict_data[AxisGraphics.X_Axis] = file_df.select(
                    data_json[AxisGraphics.X_Axis]
                ).toPandas()

            if AxisGraphics.Y_Axis in types_graphics:
                dict_data[AxisGraphics.Y_Axis] = file_df.select(
                    data_json[AxisGraphics.Y_Axis]
                ).toPandas()

        return dict_data
