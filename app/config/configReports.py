from reportlab.lib.units import cm, inch
from dataclasses import dataclass


@dataclass
class TittleReport:
    TITTLE_X: float = 10 * inch
    TITTLE_Y: float = 1 * inch
    TITTLE_FONT_SIZE: int = 20
    TITTLE_FONT: str = "Times-Roman"


@dataclass
class SubTittleReport:
    SUBTITTLE_X: float = 9 * inch
    SUBTITTLE_Y: float = 1 * inch
    SUBTITTLE_FONT_SIZE: int = 15
    SUBTITTLE_FONT: str = "Courier"


@dataclass
class SingleIMG:
    IMG_X: int = 0
    IMG_Y: int = 0
    IMG_SIZE_X: float = 15*cm
    IMG_SIZE_Y: float = 15*cm
