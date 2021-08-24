from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


def create_plot(pandas_x_df: DataFrame, pandas_y_df: DataFrame, path_img: str) -> NoReturn:
    x_name = pandas_x_df.columns[0]
    y_name = pandas_y_df.columns[0]
    plt.plot(pandas_x_df, pandas_y_df, label=f"{y_name} stock price in {x_name}", linewidth=3)
    plt.ylabel("Price")
    plt.title("Plotting Stocks")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig(path_img)
