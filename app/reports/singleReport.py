from reportlab.pdfgen.canvas import Canvas
from pandas import DataFrame
from typing import NoReturn, Optional, List
from app.reports.baseReport import BaseReport
from app.config.configReports import SingleIMG


class SingleReport(BaseReport, SingleIMG):
    def set_single_img(self, canvas: Canvas, path_img: str):
        canvas.drawImage(path_img, self.IMG_X, self.IMG_Y, self.IMG_SIZE_X, self.IMG_SIZE_Y)

    def create_report(self, pandas_df: DataFrame, path_pdf: str, path_img: List[str], other_info: Optional[dict] = None) -> NoReturn:
        x_name = pandas_df.columns[0]
        canvas = Canvas(path_pdf, pagesize=self.type_sheet)
        self.set_tittle(canvas, f"Single report for {x_name} stock")
        self.set_datetime(canvas)
        self.set_subtittle(canvas, f"Total data {pandas_df[x_name].count()}")
        if other_info:
            self.set_info(canvas, other_info)
        self.set_single_img(canvas, path_img[0])
        canvas.save()
