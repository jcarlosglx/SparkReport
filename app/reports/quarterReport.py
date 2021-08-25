from reportlab.pdfgen.canvas import Canvas
from pandas import DataFrame
from typing import NoReturn, Optional, List
from app.reports.baseReport import BaseReport
from app.config.configReports import QuarterIMG


class QuarterReport(BaseReport, QuarterIMG):
    def set_quarter_img(self, canvas: Canvas, path_img: str):
        canvas.drawImage(path_img, self.IMG_X, self.IMG_Y, self.IMG_SIZE_X, self.IMG_SIZE_Y)

    def quarter_report_pdf(self, pandas_df: DataFrame, path_pdf: str, paths_img: List[str], other_info: Optional[dict] = None) -> NoReturn:
        x_name = pandas_df.columns[0]
        canvas = Canvas(path_pdf, pagesize=self.type_sheet)
        self.set_tittle(canvas, f"Single report for {x_name} stock")
        self.set_datetime(canvas)
        self.set_subtittle(canvas, f"Total data {pandas_df[x_name].count()}")
        if other_info:
            self.set_info(canvas, other_info)
        for path_img in paths_img:
            print(f"x: {self.IMG_X} y: {self.IMG_Y}")
            self.set_quarter_img(canvas, path_img)
            self.next_quarter()
        self.reset_coordinates()
        canvas.save()
