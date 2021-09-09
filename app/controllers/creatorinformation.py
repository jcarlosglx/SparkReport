from typing import Dict, List, Type
from app.config.configGraphics import AxisGraphics, Graphics, NonGraphics
from app.graphics.graphics import GraphicName


class CreatorInformation:
    def are_create_graphics(self, result_graph: List) -> bool:
        for result in result_graph:
            if not result:
                return False
        return True

    def create_graphics(
        self, paths: List[str], data: Dict, graphics: List[str]
    ) -> List[bool]:
        results = []
        stock_graphic = GraphicName()
        x_axis = data.get(AxisGraphics.X_Axis)
        y_axis = data.get(AxisGraphics.Y_Axis)

        for path, graphic in zip(paths, graphics):
            results.append(stock_graphic.create_graphic(graphic, path, x_axis, y_axis))
        return results

    def create_non_graphics(
        self, data: Dict, non_graphics: List[str]
    ) -> Dict[str, str]:
        results = {}
        stock_graphic = GraphicName()
        x_axis = data.get(AxisGraphics.X_Axis)

        for non_graphic in non_graphics:
            results.update(stock_graphic.create_non_graphic(non_graphic, x_axis))
        return results
