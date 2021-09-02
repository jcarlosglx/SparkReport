from pyspark.sql.types import DateType, FloatType, StructField, StructType

stock_schema = StructType(
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
