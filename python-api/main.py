import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import earthquake, page_map

app = FastAPI()
print(__file__)
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))
print("📁 Static path:", static_path)
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(earthquake.router, prefix="/earthquakes")
app.include_router(page_map.router)

templates = Jinja2Templates(directory="templates")

@app.get("/map")
def root():
    return {"message": "API is running"}
