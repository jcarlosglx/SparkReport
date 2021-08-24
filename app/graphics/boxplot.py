from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


def create_boxplot(pandas_df: DataFrame, path_img: str) -> NoReturn:
    x_name = pandas_df.columns[0]
    plt.figure(figsize=(7, 5))
    plt.boxplot(pandas_df)
    plt.ylabel("Price")
    plt.title("Plotting Stocks")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig(path_img)