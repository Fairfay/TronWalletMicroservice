from fastapi import FastAPI
from app.api.endpoints import tron

app = FastAPI(title="Tron Wallet Microservice")

app.include_router(tron.router, prefix="/tron", tags=["tron"]) 