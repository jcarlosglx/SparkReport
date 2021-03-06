from dataclasses import dataclass
from os import environ
from os.path import abspath, dirname, join
from pathlib import Path

base_dir = abspath(dirname(__file__))
base_db = join(base_dir, "devDB.db")


@dataclass
class DBConfig(object):
    STOCK_DB: str = f"{Path(__file__).resolve().parent.parent}/database/stock.csv"
    PATH: str = "sqlite:///" + base_db
    if environ.get("PATH_DB"):
        PATH: str = environ.get("PATH_DB")
    N_DUMMY_RECORDS: int = 10


@dataclass
class DBDevConfig(DBConfig):
    pass


@dataclass
class DBDeployConfig(DBConfig):
    pass


config_db: dict = {"DEV": DBDevConfig, "DEPLOY": DBDeployConfig}
