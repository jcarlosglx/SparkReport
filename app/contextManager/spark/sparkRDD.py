from __future__ import annotations

from pyspark import SparkConf, SparkContext


class SparkRDD:
    def __init__(self, master: str = "", app_name: str = ""):
        if master == "" and app_name == "":
            config = SparkConf()
        else:
            config = SparkConf().setMaster(master).setAppName(app_name)
        self.spark_context = SparkContext(conf=config)

    def __enter__(self) -> SparkRDD:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
