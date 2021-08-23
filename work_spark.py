from app.ia.spark.sparkDF import SparkDataFrame
from pyspark.sql.types import StringType, StructType, StructField, DateType, FloatType

from os.path import abspath, dirname, join

path_base = abspath(dirname(__file__))
path_db = join(path_base, "app/database/stock.csv")
with SparkDataFrame("FinancialApp") as spark_df:
    #2012 - 01 - 12,
    schema = StructType(
        [
            StructField("Date", DateType(), True),
            StructField("AAPL", FloatType(), True),
            StructField("BA", FloatType(), True),
            StructField("T", FloatType(), True),
            StructField("MGM", FloatType(), True),
            StructField("AMZN", FloatType(), True),
            StructField("IBM", FloatType(), True),
            StructField("TSLA", FloatType(), True),
            StructField("GOOG", FloatType(), True),
            StructField("sp500", FloatType(), True),
        ]
    )

    data_file_df = spark_df.spark_session.read\
        .format("csv")\
        .option("header", True).option("delimiter", ",")\
        .schema(schema)\
        .load(path_db)
    data_file_df.printSchema()
    data_file_df.show(truncate=True)

