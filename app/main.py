from fastapi import FastAPI
from app.api import app_route

app = FastAPI()

app.include_router(app_route.router)

