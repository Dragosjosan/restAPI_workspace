from fastapi import FastAPI
from app.api.routes import items

app = FastAPI()

app.include_router(items.router)
