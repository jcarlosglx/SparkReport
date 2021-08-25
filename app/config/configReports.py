from reportlab.lib.units import cm
from reportlab.lib.pagesizes import LEGAL
from dataclasses import dataclass
weight, hight = LEGAL


@dataclass
class TittleReport:
    TITTLE_Y: float = round(hight*0.95)
    TITTLE_X: float = round(weight*0.1)
    TITTLE_FONT_SIZE: int = 20
    TITTLE_FONT: str = "Times-Roman"

    def recalculate_tittle(self, type_page: tuple):
        weight, hight = type_page
        self.TITTLE_Y: float = round(hight*0.95)
        self.TITTLE_X: float = round(weight*0.1)


@dataclass
class DateReport:
    DATE_Y: float = round(hight * 0.93)
    DATE_X: float = round(weight * 0.1)
    DATE_FONT_SIZE: int = 15
    DATE_FONT: str = "Courier"

    def recalculate_subtittle(self, type_page: tuple):
        weight, hight = type_page
        self.DATE_Y: float = round(hight * 0.93)
        self.DATE_X: float = round(weight * 0.1)


@dataclass
class SubTittleReport:
    SUBTITTLE_Y: float = round(hight*0.9)
    SUBTITTLE_X: float = round(weight*0.1)
    SUBTITTLE_FONT_SIZE: int = 15
    SUBTITTLE_FONT: str = "Courier"

    def recalculate_subtittle(self, type_page: tuple):
        weight, hight = type_page
        self.SUBTITTLE_Y: float = round(hight*0.9)
        self.SUBTITTLE_X: float = round(weight*0.1)


@dataclass
class InfoReport:
    INFO_Y: float = round(hight*0.8)
    INFO_X: float = round(weight*0.1)
    INFO_FONT_SIZE: int = 12
    INFO_FONT: str = "Helvetica"
    NEXT_LINE: int = 15

    def recalculate_info(self, type_page: tuple):
        weight, hight = type_page
        self.INFO_Y: float = round(hight * 0.8)
        self.INFO_X: float = round(weight * 0.1)


@dataclass
class SingleIMG:
    IMG_X: int = 0
    IMG_Y: int = 0
    IMG_SIZE_X: float = 22*cm
    IMG_SIZE_Y: float = 22*cm
