from reportlab.pdfgen.canvas import Canvas
from pandas import DataFrame
from typing import NoReturn, List
from app.reports.baseReport import BaseReport
from app.config.configReports import QuarterIMG


class SquareReport(BaseReport, QuarterIMG):
    def set_square_img(self, canvas: Canvas, path_img: str):
        canvas.drawImage(path_img, self.IMG_X, self.IMG_Y, self.IMG_SIZE_X, self.IMG_SIZE_Y)

    def square_report_pdf(self, pandas_df: DataFrame, path_pdf: str, paths_img: List[str]) -> NoReturn:
        x_name = pandas_df.columns[0]
        canvas = Canvas(path_pdf, pagesize=self.type_sheet)
        self.set_tittle(canvas, f"Square report for {x_name} stock")
        self.set_datetime(canvas)
        self.set_subtittle(canvas, f"Total data {pandas_df[x_name].count()}")
        for path_img in paths_img:
            self.set_square_img(canvas, path_img)
            self.next_quarter()
        self.reset_coordinates()
        canvas.save()
