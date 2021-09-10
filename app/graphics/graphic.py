from typing import Optional, Union

from pandas import DataFrame

from app.graphics.dataInformation import DataInformation
from app.graphics.oneDimensionGraphic import OneDimensionGraphic
from app.graphics.twoDimensionGraphic import TwoDimensionGraphic


class GraphicName:
    def __init__(self):
        self.one_dimension_classes_graphics = OneDimensionGraphic.__subclasses__()
        self.two_dimension_classes_graphics = TwoDimensionGraphic.__subclasses__()
        self.classes_non_graphics = list(DataInformation.__subclasses__())

        self.classes_graphics = list(self.one_dimension_classes_graphics.copy())
        self.classes_graphics.extend(list(self.two_dimension_classes_graphics))

    def _get_class_one_dimension_graphics(
        self, name_graphic: str
    ) -> Union[object, bool]:
        for cls in self.one_dimension_classes_graphics:
            if cls.__name__ == name_graphic:
                return cls()
        return False

    def _get_class_two_dimension_graphics(
        self, name_graphic: str
    ) -> Union[object, bool]:
        for cls in self.two_dimension_classes_graphics:
            if cls.__name__ == name_graphic:
                return cls()
        return False

    def _get_class_non_graphics(self, name_non_graphic: str) -> Union[object, bool]:
        for cls in self.classes_non_graphics:
            if cls.__name__ == name_non_graphic:
                return cls()
        return False

    def create_non_graphic(
        self,
        name_non_graphic: str,
        x_axis: Optional[DataFrame] = None,
    ) -> dict:
        try:
            if obj := self._get_class_non_graphics(name_non_graphic):
                method = getattr(obj, "create")
                return method(x_axis)
            else:
                return {}
        except:
            return {}

    def create_graphic(
        self,
        name_graphic: str,
        path: str,
        x_axis: Optional[DataFrame] = None,
        y_axis: Optional[DataFrame] = None,
    ) -> bool:
        try:

            if obj := self._get_class_one_dimension_graphics(name_graphic):
                method = getattr(obj, "create")
                return method(x_axis, path)

            elif obj := self._get_class_two_dimension_graphics(name_graphic):
                method = getattr(obj, "create")
                method(x_axis, y_axis, path)
                return True
            else:
                return False
        except:
            return False
