from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


class StockGraphics:
    def __init__(self, path_img: str, x_figure: int = 10, y_figure: int = 10):
        self.path_img = path_img
        self.x_figure = x_figure
        self.y_figure = y_figure

    def __template(self, tittle: str, x_df: DataFrame, y_df: DataFrame):
        plt.figure(figsize=(self.x_figure, self.y_figure))
        plt.grid()
        plt.legend(loc="upper left")
        plt.title(f"{tittle}")
        x_name = x_df.columns[0]
        y_name = y_df.columns[0]
        plt.ylabel(y_name)
        plt.xlabel(x_name)

    def create_histogram(self, pandas_df: DataFrame) -> NoReturn:
        x_name = pandas_df.columns[0]
        std = pandas_df[x_name].std()
        mean = pandas_df[x_name].mean()
        self.__template(f"Histogram Stock, std: {std} mean: {mean}", pandas_df, pandas_df)
        num_bins = 40
        plt.hist(pandas_df[x_name], num_bins, facecolor="blue")
        plt.savefig(self.path_img)

    def create_boxplot(self, pandas_df: DataFrame) -> NoReturn:
        self.__template("Plotting Stocks", pandas_df, pandas_df)
        plt.boxplot(pandas_df)
        plt.savefig(self.path_img)

    def create_scatter(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame) -> NoReturn:
        self.__template("Stock compare", pandas_x_df, pandas_y_df)
        plt.scatter(pandas_x_df, pandas_y_df)
        plt.savefig(self.path_img)

    def create_plot(self, pandas_x_df: DataFrame, pandas_y_df: DataFrame) -> NoReturn:
        self.__template("Plotting Stocks", pandas_x_df, pandas_y_df)
        plt.plot(pandas_x_df, pandas_y_df, linewidth=3)
        plt.savefig(self.path_img)
