from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from routers import earthquake, map_renderer

app = FastAPI()
app.include_router(earthquake.router, prefix="/earthquakes")
app.include_router(map_renderer.router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return {"message": "API is running"}