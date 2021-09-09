from test.base_test.baseGetTest import BaseGetGeneralTest
from typing import List, Dict


class BaseGraphicOneDimensionTest:
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Graphics: List[str] = [""]
    JSON: Dict[str, List[str]] = {
        "x": X_Axis,
        "Graphics": Graphics
    }

    def reload_json(self):
        self.JSON = {
            "x": self.X_Axis,
            "Graphics": self.Graphics
        }