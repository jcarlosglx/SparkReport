from dataclasses import dataclass, fields
from typing import List

from app.graphics.graphics import GraphicBase


@dataclass
class Graphics:
    Graphics_Allow = [cls.__name__ for cls in GraphicBase.__subclasses__()]


@dataclass
class NonGraphics:
    X_Axis: str = "x"
    Y_Axis: str = "y"
    Statistics: str = "Statistics"

    @staticmethod
    def get_values() -> List[str]:
        return [getattr(NonGraphics, field.name) for field in fields(NonGraphics)]
