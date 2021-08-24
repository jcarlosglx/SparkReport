from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import cm, inch
from reportlab.pdfgen.canvas import Canvas
from pandas import DataFrame

TITTLE_X = 10 * inch
TITTLE_Y = 1 * inch
TITTLE_FONT_SIZE = 20
TITTLE_FONT = "Times-Roman"


SUBTITTLE_X = 9 * inch
SUBTITTLE_Y = 1 * inch
SUBTITTLE_FONT_SIZE = 15
SUBTITTLE_FONT = "Courier"


def single_report_pdf(pandas_df: DataFrame, name_pdf: str, path_img: str) -> str:
    path_pdf = name_pdf
    x_name = pandas_df.columns[0]
    canvas = Canvas(name_pdf, pagesize=LETTER)
    canvas.setFont(TITTLE_FONT, TITTLE_FONT_SIZE)
    canvas.setFillColor(black)
    canvas.drawString(TITTLE_Y, TITTLE_X, f"Single report for {x_name} stock")
    canvas.setFont(SUBTITTLE_FONT, SUBTITTLE_FONT_SIZE)
    canvas.setFillColor(blue)
    canvas.drawString(SUBTITTLE_Y, SUBTITTLE_X, f"{x_name} through {x_name}")
    canvas.drawImage(path_img, 0, 0, 15*cm, 15*cm)
    canvas.save()
    return path_pdf
