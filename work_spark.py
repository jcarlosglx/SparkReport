from app.contextManager.spark.sparkDF import SparkDataFrame
from app.contextManager.img.imgFile import IMGFile
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

    # for plot
    # stock_x_df = file_df.select("Date")
    # stock_y_df = file_df.select("AMZN")
    # with IMGFile() as path_plot:
    #     pandas_stock_x_df = stock_x_df.toPandas()
    #     pandas_stock_y_df = stock_y_df.toPandas()
    #     stock_graphic = StockGraphics(path_plot)
    #     stock_graphic.create_plot(pandas_stock_x_df, pandas_stock_y_df)
    #     other_info = stock_graphic.get_statistics(pandas_stock_y_df)
    #     SingleReport().single_report_pdf(pandas_stock_y_df, "font-colors.pdf", path_plot, other_info)

    # for scatter
    # with IMGFile() as path_plot:
    #     pd_x_df = file_df.select("AMZN")
    #     pd_y_df = file_df.select("GOOG")
    #     create_scatter(pd_x_df.toPandas(), pd_y_df.toPandas(), path_plot)
    #     single_report_pdf(file_df.select("AMZN", "GOOG"), "test.pdf", path_plot)

    # for histogram
    # stock_df = file_df.select("AMZN")
    # pd_df = stock_df.toPandas()
    # with IMGFile() as path_plot:
    #     create_histogram(pd_df, path_plot)
    #     single_report_pdf(pd_df, "font-colors.pdf", path_plot)

    # for boxplot
    # stock_df = file_df.select("AMZN")
    # pd_df = stock_df.toPandas()
    # with IMGFile() as path_plot:
    #     create_boxplot(pd_df, path_plot)
    #     single_report_pdf(pd_df, "font-colors.pdf", path_plot)

    stock_x_df = file_df.select("Date")
    stock_y_df = file_df.select("AMZN", "GOOG")
    with IMGFile() as path_plot:
        pandas_stock_x_df = stock_x_df.toPandas()
        pandas_stock_y_df = stock_y_df.toPandas()
        stock_graphic = StockGraphics(path_plot)
        stock_graphic.create_multi_boxplot(pandas_stock_y_df)
        with IMGFile() as path_hist:
            single_stock = file_df.select("AMZN")
            pandas_single_stock = single_stock.toPandas()
            stock_graphic.set_path(path_hist)
            stock_graphic.create_histogram(pandas_single_stock)
            SquareReport().square_report_pdf(pandas_stock_y_df, "font-colors.pdf", [path_plot, path_hist, path_plot, path_hist, path_plot])
