from app.config.configReports import TittleReport, SubTittleReport, InfoReport, DateReport
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import blue, black, brown
from reportlab.lib.pagesizes import LEGAL
from typing import NoReturn


class BaseReport(TittleReport, SubTittleReport, InfoReport, DateReport):
    def __init__(self, type_sheet: tuple = LEGAL):
        self.type_sheet = type_sheet
        if type_sheet != LEGAL:
            self.recalculate_subtittle(type_sheet)
            self.recalculate_tittle(type_sheet)
            self.recalculate_info(type_sheet)

    def set_tittle(self, canvas: Canvas, tittle: str) -> NoReturn:
        canvas.setFont(self.TITTLE_FONT, self.TITTLE_FONT_SIZE)
        canvas.setFillColor(black)
        canvas.drawString(self.TITTLE_X, self.TITTLE_Y, f"{tittle}")

    def set_datetime(self, canvas: Canvas) -> NoReturn:
        canvas.setFont(self.DATE_FONT, self.DATE_FONT_SIZE)
        canvas.setFillColor(black)
        canvas.drawString(self.DATE_X, self.DATE_Y, f"{datetime.today().strftime('%Y-%m-%d')}")

    def set_subtittle(self, canvas: Canvas, subttitle: str) -> NoReturn:
        canvas.setFont(self.SUBTITTLE_FONT, self.SUBTITTLE_FONT_SIZE)
        canvas.setFillColor(blue)
        canvas.drawString(self.SUBTITTLE_X, self.SUBTITTLE_Y, f"{subttitle}")

    def set_info(self, canvas: Canvas, information: dict) -> NoReturn:
        canvas.setFont(self.INFO_FONT, self.INFO_FONT_SIZE)
        canvas.setFillColor(brown)
        for i, key in enumerate(information.keys()):
            canvas.drawString(self.INFO_X, self.INFO_Y + (i * self.NEXT_LINE), f"{key}: {information[key]}")
