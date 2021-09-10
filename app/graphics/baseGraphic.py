from typing import NoReturn

import matplotlib.pyplot as plt
from pandas import DataFrame


class NonGraphicsBase:
    FIRST = 0


class GraphicBase:
    def __init__(self, x_figure: int = 10, y_figure: int = 10):
        self.x_figure = x_figure
        self.y_figure = y_figure
        self.FIRST = 0

    def _single_template(
        self, tittle: str, x_df: DataFrame, y_df: DataFrame
    ) -> NoReturn:
        x_name = x_df.columns[self.FIRST]
        y_name = y_df.columns[self.FIRST]

        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def _multi_template(
        self, tittle: str, x_df: DataFrame, y_df: DataFrame
    ) -> NoReturn:
        x_name = x_df.columns[self.FIRST]
        y_name = str([f"{name} " for name in y_df.columns])
        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)
