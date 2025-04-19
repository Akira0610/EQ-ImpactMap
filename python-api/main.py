# python-api/main.py

from fastapi import FastAPI
from routers import earthquake

app = FastAPI()

app.include_router(earthquake.router, prefix="/earthquakes")

@app.get("/")
def root():
    return {"message": "API is up"}
@app.get("/ping")
def ping():
    return {"status": "pong"}
