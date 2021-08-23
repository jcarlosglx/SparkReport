from app.contextManager.spark.sparkDF import SparkDataFrame
from app.contextManager.img.imgFile import IMGFile
from os.path import abspath, dirname, join
from app.schemas.stockSchema import stock_schema
from app.reports.singleReport import single_report_pdf
from app.graphics.plot import create_plot

path_base = abspath(dirname(__file__))
path_db = join(path_base, "app/database/stock.csv")

with SparkDataFrame("FinancialApp") as spark_df:
    file_df = spark_df.spark_session.read\
        .format("csv")\
        .option("header", True).option("delimiter", ",")\
        .schema(stock_schema)\
        .load(path_db)
    # file_df.printSchema()
    # file_df.show(truncate=True)

    stock_df = file_df.select("Date", "AMZN")
    pd_df = stock_df.toPandas()
    with IMGFile() as path_plot:
        create_plot(pd_df, path_plot)
        single_report_pdf(pd_df, "font-colors.pdf", path_plot)
