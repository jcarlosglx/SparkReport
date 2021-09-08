from dataclasses import dataclass, fields
from typing import List

from app.graphics.graphics import GraphicName


@dataclass
class Graphics:
    Graphics_Allow = [cls.__name__ for cls in GraphicName().classes]


@dataclass
class NonGraphics:
    X_Axis: str = "x"
    Y_Axis: str = "y"
    Statistics: str = "Statistics"

    @staticmethod
    def get_values() -> List[str]:
        return [getattr(NonGraphics, field.name) for field in fields(NonGraphics)]
