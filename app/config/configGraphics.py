from dataclasses import dataclass
from typing import Tuple


@dataclass
class TypesGraphics:
    TypesGraphics: Tuple[str] = (
        "Histogram",
        "Boxplot",
        "Multi-Boxplot",
        "Scatter",
        "Plot",
        "Multi-Plot",
        "Statistics",
    )
