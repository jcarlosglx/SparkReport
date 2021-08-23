from app.ia.spark.sparkDF import SparkDataFrame
from pyspark.sql.types import StructType, StructField, DateType, FloatType
import matplotlib.pyplot as plt
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

    file_df = spark_df.spark_session.read\
        .format("csv")\
        .option("header", True).option("delimiter", ",")\
        .schema(schema)\
        .load(path_db)
    file_df.printSchema()
    file_df.show(truncate=True)

    stock_df = file_df.select("Date", "AMZN")
    pandas_df = file_df.toPandas()
    pandas_df.plot(x="Date", y="AMZN", label="AMAZN stock Price", linewidth=3)
    plt.ylabel("Price")
    plt.title("Plotting Stocks")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig(join(path_base, "Prueba-x.png"))