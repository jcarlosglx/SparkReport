from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, NoReturn, Optional

from pandas import DataFrame
from reportlab.lib.colors import black, blue, brown
from reportlab.lib.pagesizes import LEGAL
from reportlab.pdfgen.canvas import Canvas

from app.config.configReports import (DateReport, InfoReport, SubTittleReport,
                                      TittleReport)


class BaseReport(TittleReport, SubTittleReport, InfoReport, DateReport, ABC):
    def __init__(self, type_sheet: tuple = LEGAL):
        self.type_sheet = type_sheet
        if type_sheet != LEGAL:
            self.recalculate_subtittle(type_sheet)
            self.recalculate_tittle(type_sheet)
            self.recalculate_info(type_sheet)

    @abstractmethod
    def create_report(
        self,
        pandas_df: DataFrame,
        path_pdf: str,
        path_img: List[str],
        other_info: Optional[dict] = None,
    ) -> NoReturn:
        pass

    def set_tittle(self, canvas: Canvas, tittle: str) -> NoReturn:
        canvas.setFont(self.TITTLE_FONT, self.TITTLE_FONT_SIZE)
        canvas.setFillColor(black)
        canvas.drawString(self.TITTLE_X, self.TITTLE_Y, f"{tittle}")

    def set_datetime(self, canvas: Canvas) -> NoReturn:
        canvas.setFont(self.DATE_FONT, self.DATE_FONT_SIZE)
        canvas.setFillColor(black)
        canvas.drawString(
            self.DATE_X,
            self.DATE_Y,
            f"Date report: {datetime.today().strftime('%Y-%m-%d')}",
        )

    def set_subtittle(self, canvas: Canvas, subttitle: str) -> NoReturn:
        canvas.setFont(self.SUBTITTLE_FONT, self.SUBTITTLE_FONT_SIZE)
        canvas.setFillColor(blue)
        canvas.drawString(self.SUBTITTLE_X, self.SUBTITTLE_Y, f"{subttitle}")

    def set_info(self, canvas: Canvas, information: dict) -> NoReturn:
        canvas.setFont(self.INFO_FONT, self.INFO_FONT_SIZE)
        canvas.setFillColor(brown)
        for i, key in enumerate(information.keys()):
            canvas.drawString(
                self.INFO_X,
                self.INFO_Y + (i * self.NEXT_LINE),
                f"{key}: {information[key]}",
            )
