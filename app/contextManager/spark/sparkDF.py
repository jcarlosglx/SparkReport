from __future__ import annotations
from pyspark.sql import SparkSession


class SparkDataFrame:
    def __init__(self, app_name: str = ""):
        self.spark_session = SparkSession.builder.appName(app_name).getOrCreate()

    def __enter__(self) -> SparkDataFrame:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark_session.stop()
