from typing import NoReturn, Optional
from pandas import DataFrame
import matplotlib.pyplot as plt


class StockGraphics:
    def __init__(self, x_figure: int = 10, y_figure: int = 10):
        self.x_figure = x_figure
        self.y_figure = y_figure
        self.FIRST = 0

    def __single_template(self, tittle: str, x_df: DataFrame, y_df: DataFrame) -> NoReturn:
        x_name = x_df.columns[self.FIRST]
        y_name = y_df.columns[self.FIRST]

        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def __multi_template(self, tittle: str, x_df: DataFrame, y_df: DataFrame) -> NoReturn:
        x_name = x_df.columns[self.FIRST]
        y_name = str([f"{name} " for name in y_df.columns])
        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def create_graphic(self, name_graphic: str, path: str, x_axis: Optional[str] = None, y_axis: Optional[str] = None) -> bool:
        try:
            if x_axis:
                method = getattr(self, name_graphic)
                method(y_axis, path)
            elif x_axis and y_axis:
                method = getattr(self, name_graphic)
                method(x_axis, y_axis, path)
                return True
        except:
            return False

    def statistics(self, pandas_df: DataFrame) -> dict:
        try:
            name = pandas_df.columns[self.FIRST]
            return {
                "mean": pandas_df[name].mean(),
                "median": pandas_df[name].median(),
                "mode": round(pandas_df[name].mode()[self.FIRST], 5),
                "std": pandas_df[name].std(),
                "max": pandas_df[name].max(),
                "min": pandas_df[name].min()
            }
        except:
            return {}

    def histogram(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            x_name = pandas_df.columns[self.FIRST]
            self.__single_template("Histogram Stock", pandas_df, pandas_df)
            num_bins = 40
            plt.hist(pandas_df[x_name], num_bins, facecolor="blue")
            plt.savefig(path)
            return True
        except:
            return False

    def boxplot(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self.__single_template("Plotting Stocks", pandas_df, pandas_df)
            plt.boxplot(pandas_df)
            plt.savefig(path)
            return True
        except:
            return False

    def multi_boxplot(self, pandas_df: DataFrame, path: str) -> bool:
        try:
            self.__multi_template("Plotting Stocks", pandas_df, pandas_df)
            labels = [f"{name}" for name in pandas_df.columns]
            plt.boxplot(pandas_df, labels=labels)
            plt.savefig(path)
            return True
        except:
            return False

    def scatter(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self.__single_template("Stock compare", pandas_x_df, pandas_y_df)
            plt.scatter(pandas_x_df, pandas_y_df)
            plt.savefig(path)
        except:
            return False

    def plot(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self.__single_template("Plotting Stocks", pandas_x_df, pandas_y_df)
            name = pandas_y_df.columns[self.FIRST]
            plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
            plt.legend(loc="upper left")
            plt.savefig(path)
            return True
        except:
            return False

    def multi_plot(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame, path: str) -> bool:
        try:
            self.__multi_template("Plotting Stocks", pandas_x_df, pandas_y_df)
            name = pandas_y_df.columns
            plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
            plt.legend(loc="upper left")
            plt.savefig(path)
            return True
        except:
            return False
