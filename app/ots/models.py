from sqlalchemy import Column, Integer, String, DATETIME
import datetime
from app.ots.database import Base

""" 
CREATE TABLE ots_contents (
    seq bigint NOT NULL AUTO_INCREMENT,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    duration int DEFAULT NULL,
    expire_at datetime DEFAULT NULL,
    phrase varchar(1000) DEFAULT NULL,
    urlpath varchar(200) NOT NULL,
    content text DEFAULT '',
    modified_at datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP(),
    is_valid bool DEFAULT true,
    PRIMARY KEY (seq),
    CONSTRAINT unq_ots_urlpath UNIQUE (urlpath)
)
"""


class Ots(Base):
    __tablename__ = "ots"

    id = Column(Integer, primary_key=True, index=True)
    duration_seconds = Column(Integer)
    expire_at = Column(DATETIME)
    phrase = Column(String)
    urlpath = Column(String, unique=True)
    content = Column(String, default='')
    created_at = Column(DATETIME, index=True, default=datetime.datetime.now)
    modified_at = Column(DATETIME, default=datetime.datetime.now, onupdate=datetime.datetime.now)
