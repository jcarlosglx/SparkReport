from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


class StockGraphics:
    def __init__(self, path_img: str, x_figure: int = 10, y_figure: int = 10):
        self.path_img = path_img
        self.x_figure = x_figure
        self.y_figure = y_figure

    def __single_template(self, tittle: str, x_df: DataFrame, y_df: DataFrame) -> NoReturn:
        x_name = x_df.columns[0]
        y_name = y_df.columns[0]
        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def __multi_template(self, tittle: str, x_df: DataFrame, y_df: DataFrame) -> NoReturn:
        x_name = x_df.columns[0]
        y_name = str([f"{name} " for name in y_df.columns])
        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.title(f"{tittle}")
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def set_path(self, new_path: str) -> NoReturn:
        self.path_img = new_path

    def get_statistics(self, pandas_df: DataFrame) -> dict:
        name = pandas_df.columns[0]
        return {
            "mean": pandas_df[name].mean(),
            "median": pandas_df[name].median(),
            "mode": round(pandas_df[name].mode()[0], 5),
            "std": pandas_df[name].std(),
            "max": pandas_df[name].max(),
            "min": pandas_df[name].min()
        }

    def create_histogram(self, pandas_df: DataFrame) -> NoReturn:
        x_name = pandas_df.columns[0]
        self.__single_template("Histogram Stock", pandas_df, pandas_df)
        num_bins = 40
        plt.hist(pandas_df[x_name], num_bins, facecolor="blue")
        plt.savefig(self.path_img)

    def create_boxplot(self, pandas_df: DataFrame) -> NoReturn:
        self.__single_template("Plotting Stocks", pandas_df, pandas_df)
        plt.boxplot(pandas_df)
        plt.savefig(self.path_img)

    def create_multi_boxplot(self, pandas_df: DataFrame) -> NoReturn:
        self.__multi_template("Plotting Stocks", pandas_df, pandas_df)
        labels = [f"{name}" for name in pandas_df.columns]
        plt.boxplot(pandas_df, labels=labels)
        plt.savefig(self.path_img)

    def create_scatter(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame) -> NoReturn:
        self.__single_template("Stock compare", pandas_x_df, pandas_y_df)
        plt.scatter(pandas_x_df, pandas_y_df)
        plt.savefig(self.path_img)

    def create_plot(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame) -> NoReturn:
        self.__single_template("Plotting Stocks", pandas_x_df, pandas_y_df)
        name = pandas_y_df.columns[0]
        plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
        plt.legend(loc="upper left")
        plt.savefig(self.path_img)

    def create_multi_plot(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame) -> NoReturn:
        self.__multi_template("Plotting Stocks", pandas_x_df, pandas_y_df)
        name = pandas_y_df.columns
        plt.plot(pandas_x_df, pandas_y_df, label=name, linewidth=3)
        plt.legend(loc="upper left")
        plt.savefig(self.path_img)
