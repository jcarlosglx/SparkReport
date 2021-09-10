from test.base_test.base_http.baseGetTest import BaseGetGeneralTest
from typing import Dict, List

from app.graphics.oneDimensionGraphic import OneDimensionGraphic


class BaseGraphicOneDimensionTest:
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Graphics: List[str] = [""]
    JSON: Dict[str, List[str]] = {"x": X_Axis, "Graphics": Graphics}
    TypeGraphics: List[str] = [
        cls.__name__ for cls in OneDimensionGraphic.__subclasses__()
    ]

    def reload_json(self):
        self.JSON = {"x": self.X_Axis, "Graphics": self.Graphics}
