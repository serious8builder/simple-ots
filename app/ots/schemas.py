

from pydantic import BaseModel
from datetime import datetime

""" 
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DATETIME, index=True)
    duration_seconds = Column(Integer)
    expire_at = Column(DATETIME)
    phrase = Column(String)
    urlpath = Column(String, unique=True)
    content = Column(String, default='')
    modified_at = Column(DATETIME)

"""


class OtsBase(BaseModel):
    phrase: str
    content: str


class OtsCreate(OtsBase):
    duration_seconds: int


class Ots(OtsBase):
    id: int
    urlpath: str
    created_at: datetime
    modified_at: datetime
    expire_at: datetime

    class Config:
        orm_mode = True
