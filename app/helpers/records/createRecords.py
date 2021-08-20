from typing import NoReturn

from app.helpers.records.dummyRecords import get_dummy_record
from app.models.entryORM import db
from app.models.logModel import LogModel


def create_records(size: int) -> NoReturn:
    for n in range(1, size + 1):
        new_log = get_dummy_record(n, LogModel)
        db.session.add(new_log)
        db.session.commit()
