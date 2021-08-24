from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


def create_scatter(pandas_x_df: DataFrame, pandas_y_df: DataFrame, path_img: str) -> NoReturn:
    x_name = pandas_x_df.columns[0]
    y_name = pandas_y_df.columns[0]
    plt.xlabel(f"Stock of {x_name}")
    plt.ylabel(f"Stock of {y_name}")
    plt.title(f"Stock compare")
    plt.legend(loc="upper left")
    plt.scatter(pandas_x_df, pandas_y_df)
    plt.grid()
    plt.savefig(path_img)