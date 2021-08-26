from app.contextManager.spark.sparkDF import SparkDataFrame
from app.contextManager.path.files import PathFiles
from os.path import abspath, dirname, join
from app.schemas.stockSchema import stock_schema
from app.reports.singleReport import SingleReport
from app.reports.squareReport import SquareReport
from app.reports.quarterReport import QuarterReport
from app.graphics.stockGraphics import StockGraphics

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

    stock_x_df = file_df.select("Date")
    stock_y_multi_df = file_df.select("AMZN", "GOOG", "TSLA")
    stock_y_single_df = file_df.select("AMZN")
    with PathFiles(5) as paths:
        pandas_single_y_df = stock_y_single_df.toPandas()
        pandas_multi_y_df = stock_y_multi_df.toPandas()
        pandas_x_df = stock_x_df.toPandas()
        stock_graphic = StockGraphics()
        stock_graphic.create_boxplot(pandas_single_y_df, paths[0])
        stock_graphic.create_plot(pandas_x_df, pandas_single_y_df, paths[1])
        stock_graphic.create_multi_plot(pandas_x_df, pandas_multi_y_df, paths[2])
        stock_graphic.create_multi_boxplot(pandas_multi_y_df, paths[3])
        stock_graphic.create_histogram(pandas_single_y_df, paths[4])
        other_data = stock_graphic.get_statistics(pandas_single_y_df)
        SingleReport().single_report_pdf(pandas_single_y_df, "single.pdf", paths[0], other_data)
        SquareReport().square_report_pdf(pandas_single_y_df, "square.pdf", paths)
        QuarterReport().quarter_report_pdf(pandas_single_y_df, "quarter.pdf", paths[0:4], other_data)
