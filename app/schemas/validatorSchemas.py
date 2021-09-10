from typing import List

from app.config.configGraphics import Graphics, NonGraphics


def validate_graphics_name(list_graphics: List[str]) -> bool:
    for graphic in list_graphics:
        if graphic not in Graphics.Graphics_Allow:
            return False
    return True


def validate_non_graphics_name(list_non_graphics: List[str]) -> bool:
    for graphic in list_non_graphics:
        if graphic not in NonGraphics.Non_Graphics_Allow:
            return False
    return True
