from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


def create_plot(pandas_df: DataFrame, path_img: str) -> NoReturn:
    x_name = pandas_df.columns[0]
    y_name = pandas_df.columns[1]
    pandas_df.plot(x=x_name, y=y_name, label=f"{y_name} stock price", linewidth=3)
    plt.ylabel("Price")
    plt.title("Plotting Stocks")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig(path_img)
