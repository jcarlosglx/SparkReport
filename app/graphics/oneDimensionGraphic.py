from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
from pandas import DataFrame

from app.graphics.baseGraphic import GraphicBase


class OneDimensionGraphic(ABC, GraphicBase):
    @abstractmethod
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        pass


class Histogram(OneDimensionGraphic):
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            x_name = pandas_df.columns[self.FIRST]
            self._single_template("Histogram Stock", pandas_df, pandas_df)
            num_bins = 40
            plt.hist(pandas_df[x_name], num_bins, facecolor="blue")
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()


class BoxPlot(OneDimensionGraphic):
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self._single_template("Plotting Stocks", pandas_df, pandas_df)
            plt.boxplot(pandas_df)
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()


class MultiBoxPlot(OneDimensionGraphic):
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self._multi_template("Plotting Stocks", pandas_df, pandas_df)
            labels = [f"{name}" for name in pandas_df.columns]
            plt.boxplot(pandas_df, labels=labels)
            plt.savefig(path)
            return True
        except:
            return False
        finally:
            plt.close()
