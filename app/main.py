from fastapi import FastAPI

from.check.routers import health

app = FastAPI()

app.include_router(health.router, prefix='/check')