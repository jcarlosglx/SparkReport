from abc import abstractmethod
from typing import NoReturn, Optional

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

    def create_element(self):
        pass

    def create_graphic(
        self,
        name_graphic: str,
        path: str,
        x_axis: Optional[DataFrame] = None,
        y_axis: Optional[DataFrame] = None,
    ) -> bool:
        try:
            for cls in GraphicBase.__subclasses__():
                if cls.__name__ == name_graphic:
                    obj = cls()
                    break
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


class Statistics(NonGraphicsBase):
    def create(self, pandas_df: DataFrame) -> dict:
        try:
            name = pandas_df.columns[self.FIRST]
            return {
                "mean": pandas_df[name].mean(),
                "median": pandas_df[name].median(),
                "mode": round(pandas_df[name].mode()[self.FIRST], 5),
                "std": pandas_df[name].std(),
                "max": pandas_df[name].max(),
                "min": pandas_df[name].min(),
            }
        except:
            return {}


class Histogram(GraphicBase):
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


class BoxPlot(GraphicBase):
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self._single_template("Plotting Stocks", pandas_df, pandas_df)
            plt.boxplot(pandas_df)
            plt.savefig(path)
            return True
        except:
            return False


class MultiBoxPlot(GraphicBase):
    def create(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self._multi_template("Plotting Stocks", pandas_df, pandas_df)
            labels = [f"{name}" for name in pandas_df.columns]
            plt.boxplot(pandas_df, labels=labels)
            plt.savefig(path)
            return True
        except:
            return False


class Scatter(GraphicBase):
    def create(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self._single_template("Stock compare", pandas_x_df, pandas_y_df)
            plt.scatter(pandas_x_df, pandas_y_df)
            plt.savefig(path)
        except:
            return False


class Plot(GraphicBase):
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


class MultiPlot(GraphicBase):
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
