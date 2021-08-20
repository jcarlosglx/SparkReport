from typing import NoReturn

from app.models.entryORM import db


def delete_records() -> NoReturn:
    db.drop_all()
    # Code for postgresql
    # for table in database.metadata.tables.keys():
    #     database.session.execute(f"TRUNCATE TABLE {table} CASCADE")
    #     database.session.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
    # database.session.commit()
