from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from pandas import DataFrame
from typing import NoReturn
from app.config.configReports import TittleReport, SubTittleReport, SingleIMG


class SingleReport(TittleReport, SubTittleReport, SingleIMG):
    def __init__(self, type_sheet: tuple = LETTER):
        self.type_sheet = type_sheet

    def set_tittle(self, canvas: Canvas, tittle: str) -> NoReturn:
        canvas.setFont(self.TITTLE_FONT, self.TITTLE_FONT_SIZE)
        canvas.setFillColor(black)
        canvas.drawString(self.TITTLE_Y, self.TITTLE_X, f"{tittle}")

    def set_subtittle(self, canvas: Canvas, subttitle: str) -> NoReturn:
        canvas.setFont(self.SUBTITTLE_FONT, self.SUBTITTLE_FONT_SIZE)
        canvas.setFillColor(blue)
        canvas.drawString(self.SUBTITTLE_Y, self.SUBTITTLE_X, f"{subttitle}")

    def set_single_img(self, canvas: Canvas, path_img: str):
        canvas.drawImage(path_img, self.IMG_X, self.IMG_Y, self.IMG_SIZE_X, self.IMG_SIZE_Y)

    def single_report_pdf(self, pandas_df: DataFrame, path_pdf: str, path_img: str) -> NoReturn:
        x_name = pandas_df.columns[0]
        canvas = Canvas(path_pdf, pagesize=self.type_sheet)
        self.set_tittle(canvas, f"Single report for {x_name} stock")
        self.set_subtittle(canvas, f"{x_name} through {x_name}")
        self.set_single_img(canvas, path_img)
        canvas.save()
