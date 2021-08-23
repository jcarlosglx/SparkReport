from app.ia.spark.sparkDF import SparkDataFrame
import matplotlib.pyplot as plt
from os.path import abspath, dirname, join
from app.schemas.stockSchema import stock_schema
from uuid import uuid4
from pandas import DataFrame
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import cm, inch
from reportlab.pdfgen.canvas import Canvas


def create_plot(pandas_df: DataFrame) -> str:
    pandas_df.plot(x="Date", y="AMZN", label="AMAZN stock Price", linewidth=3)
    plt.ylabel("Price")
    plt.title("Plotting Stocks")
    plt.legend(loc="upper left")
    plt.grid()
    name_file = f"{uuid4()}.png"
    plt.savefig(join(path_base, name_file))
    return name_file


def create_pdf(name_pdf: str, path_img: str) -> str:
    path_pdf = name_pdf

    canvas = Canvas(name_pdf, pagesize=LETTER)

    # Set font to Times New Roman with 12-point size
    canvas.setFont("Times-Roman", 12)

    # Draw blue text one inch from the left and ten
    # inches from the bottom
    canvas.setFillColor(blue)
    # canvas.drawString(1 * inch, 10 * inch, "Blue text")
    canvas.drawImage(path_img, 0, 0, 10*cm, 10*cm)
    # Save the PDF file
    canvas.save()
    return path_pdf


path_base = abspath(dirname(__file__))
path_db = join(path_base, "app/database/stock.csv")

with SparkDataFrame("FinancialApp") as spark_df:
    file_df = spark_df.spark_session.read\
        .format("csv")\
        .option("header", True).option("delimiter", ",")\
        .schema(stock_schema)\
        .load(path_db)
    file_df.printSchema()
    file_df.show(truncate=True)

    stock_df = file_df.select("Date", "AMZN")
    pd_df = file_df.toPandas()
    create_pdf("font-colors.pdf", create_plot(pd_df))
