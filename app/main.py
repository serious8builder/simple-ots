from fastapi import FastAPI

from .check.routers import health
from .ots.routers import ots
from .ots.database import engine, Base

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(health.router, prefix='/check')
app.include_router(ots.router, prefix='/ots')
