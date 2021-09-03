from dataclasses import dataclass, fields
from typing import List

@dataclass
class Graphics:
    Histogram: str = "histogram"
    Boxplot: str = "boxplot"
    MultiBoxplot: str = "multi_boxplot"
    Scatter: str = "scatter"
    Plot: str = "plot"
    MultiPlot: str = "multi_plot"

    @staticmethod
    def get_values() -> List[str]:
        return [getattr(Graphics, field.name) for field in fields(Graphics)]

@dataclass
class NonGraphics:
    X_Axis: str = "x"
    Y_Axis: str = "y"
    Statistics: str = "statistics"

    @staticmethod
    def get_values() -> List[str]:
        return [getattr(NonGraphics, field.name) for field in fields(NonGraphics)]
