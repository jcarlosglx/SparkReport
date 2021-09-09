from test.base_test.baseGetTest import BaseGetGeneralTest
from typing import List, Dict


class BaseGraphicTwoDimensionTest:
    X_Axis: List[str] = [BaseGetGeneralTest.header_cvs[1]]
    Y_Axis: List[str] = [BaseGetGeneralTest.header_cvs[2]]
    Graphics: List[str] = [""]
    JSON: Dict[str, List[str]] = {
        "x": X_Axis,
        "y": Y_Axis,
        "Graphics": Graphics
    }

    def reload_json(self):
        self.JSON = {
            "x": self.X_Axis,
            "y": self.Y_Axis,
            "Graphics": self.Graphics
        }