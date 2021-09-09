from typing import Dict, List, Type

from app.config.configGraphics import AxisGraphics, Graphics, NonGraphics


class ParserInformation:
    def get_graphics(self, data: Dict) -> List[str]:
        graphic_allow = Graphics.Graphics_Allow
        list_graphics = []
        if graphics := data.get("Graphics"):
            list_graphics = [
                graphic for graphic in graphics if graphic in graphic_allow
            ]
        return list_graphics

    def get_non_graphics(self, data: Dict) -> List[str]:
        non_graphic_allow = NonGraphics.Non_Graphics_Allow
        list_graphics = []
        if graphics := data.get("Graphics"):
            list_graphics = [
                graphic for graphic in graphics if graphic in non_graphic_allow
            ]
        return list_graphics

    def get_axis(self, data: Dict) -> List[str]:
        names = []
        keys = AxisGraphics.get_values()
        for axis in data.keys():
            if axis in keys:
                names.append(axis)
        return names
