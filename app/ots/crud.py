from sqlalchemy.orm import Session
import datetime
import uuid

from . import models, schemas


def get_ots(ots_id: int, db: Session):
    return db.query(models.Ots).filter(models.Ots.id == ots_id).first()


def create_ots(ots: schemas.OtsCreate, db: Session):
    expire_at = datetime.datetime.now() + datetime.timedelta(seconds=ots.duration_seconds)
    urlpath = uuid.uuid4().hex
    db_ots = models.Ots(
        duration_seconds=ots.duration_seconds,
        phrase=ots.phrase,
        content=ots.content,
        urlpath=urlpath,
        expire_at=expire_at
    )
    db.add(db_ots)
    db.commit()
    db.refresh(db_ots)
    response = {
        'path': db_ots.urlpath,
        'expire': db_ots.expire_at,
    }
    return response


def reveal_secret(path: str, db: Session):
    ots = db.query(models.Ots).filter(models.Ots.urlpath == path).first()
    secret = ots.content
    response = {
        'seecret': secret
    }

    return response
