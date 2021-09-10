from app.graphics.oneDimensionGraphic import OneDimensionGraphic
from app.graphics.twoDimensionGraphic import TwoDimensionGraphic
from app.graphics.dataInformation import DataInformation
from typing import Optional, Union
from pandas import DataFrame


class GraphicName:
    def __init__(self):
        self.classes_graphics = list(OneDimensionGraphic.__subclasses__())
        self.classes_graphics.extend(list(TwoDimensionGraphic.__subclasses__()))

        self.classes_non_graphics = list(DataInformation.__subclasses__())

    def _get_class_graphics(self, name_graphic: str) -> Union[object, bool]:
        for cls in self.classes_graphics:
            if cls.__name__ == name_graphic:
                return cls()
        return False

    def _get_class_non_graphics(self, name_graphic: str) -> Union[object, bool]:
        for cls in self.classes_graphics:
            if cls.__name__ == name_graphic:
                return cls()
        return False

    def create_non_graphic(
            self,
            name_non_graphic: str,
            x_axis: Optional[DataFrame] = None,
    ) -> dict:
        try:

            obj = self._get_class_non_graphics(name_non_graphic)
            if not obj:
                return {}

            if isinstance(x_axis, DataFrame):
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

            obj = self._get_class_graphics(name_graphic)
            if not obj:
                return False

            if isinstance(x_axis, DataFrame) and not isinstance(y_axis, DataFrame):
                method = getattr(obj, "create")
                return method(x_axis, path)

            elif isinstance(x_axis, DataFrame) and isinstance(y_axis, DataFrame):
                method = getattr(obj, "create")
                method(x_axis, y_axis, path)
                return True
            else:
                return False
        except:
            return False
