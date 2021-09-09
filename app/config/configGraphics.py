from dataclasses import dataclass, fields
from typing import List

from app.graphics.graphics import GraphicName


@dataclass
class Graphics:
    Graphics_Allow = [cls.__name__ for cls in GraphicName().classes_graphics]


@dataclass
class AxisGraphics:
    X_Axis: str = "x"
    Y_Axis: str = "y"

    @staticmethod
    def get_values() -> List[str]:
        return [getattr(AxisGraphics, field.name) for field in fields(AxisGraphics)]

@dataclass
class NonGraphics:
    Non_Graphics_Allow = [cls.__name__ for cls in GraphicName().classes_non_graphics]

