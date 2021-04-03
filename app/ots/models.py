from sqlalchemy import Column, Integer, String, DATETIME, TEXT
import datetime
from app.ots.database import Base


class Ots(Base):
    __tablename__ = "ots"

    id = Column(Integer, primary_key=True, index=True)
    duration_seconds = Column(Integer)
    expire_at = Column(DATETIME)
    phrase = Column(String(200))
    urlpath = Column(String(23), unique=True)
    content = Column(TEXT, default='')
    created_at = Column(DATETIME, index=True, default=datetime.datetime.now)
    modified_at = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)
