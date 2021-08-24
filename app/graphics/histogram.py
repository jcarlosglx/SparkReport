from typing import NoReturn
from pandas import DataFrame
import matplotlib.pyplot as plt


def create_histogram(pandas_df: DataFrame, path_img: str) -> NoReturn:
    x_name = pandas_df.columns[0]
    std = pandas_df[x_name].std()
    mean = pandas_df[x_name].mean()
    num_bins = 40
    plt.figure(figsize=(7, 5))
    plt.hist(pandas_df[x_name], num_bins, facecolor="blue")
    plt.grid()
    plt.ylabel("Probability")
    plt.title(f"Histogram Stock, std: {std} mean: {mean}")
    plt.savefig(path_img)
