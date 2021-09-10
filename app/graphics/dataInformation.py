from app.graphics.baseGraphic import GraphicBase
from abc import ABC, abstractmethod

from pandas import DataFrame

class DataInformation(ABC, GraphicBase):
    @abstractmethod
    def create(self, pandas_df: DataFrame) -> dict:
        pass


class Statistics(DataInformation):
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
