from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
from pandas import DataFrame

from app.graphics.baseGraphic import GraphicBase


class TwoDimensionGraphic(ABC, GraphicBase):
    @abstractmethod
    def create(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        pass


class Scatter(TwoDimensionGraphic):
    def create(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self._single_template("Stock compare", pandas_x_df, pandas_y_df)
            plt.scatter(pandas_x_df, pandas_y_df)
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()


class Plot(TwoDimensionGraphic):
    def create(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self._single_template("Plotting Stocks", pandas_x_df, pandas_y_df)
            name = pandas_y_df.columns[self.FIRST]
            plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
            plt.legend(loc="upper left")
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()


class MultiPlot(TwoDimensionGraphic):
    def create(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self._multi_template("Plotting Stocks", pandas_x_df, pandas_y_df)
            name = pandas_y_df.columns
            plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
            plt.legend(loc="upper left")
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()
