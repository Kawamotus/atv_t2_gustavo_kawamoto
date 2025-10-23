from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="ATV 2 - Gustavo Kawamoto")

app.include_router(router)
