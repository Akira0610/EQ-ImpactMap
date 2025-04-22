import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import earthquake, page_map

app = FastAPI()

# ✅ 掛載靜態檔案（指向 EQIDV_fronted/public）
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../EQIDV_fronted/public"))
app.mount("/static", StaticFiles(directory=static_path), name="static")

# ✅ 掛載路由
app.include_router(earthquake.router, prefix="/earthquakes")
app.include_router(page_map.router)

# ✅ 啟用模板渲染
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return {"message": "API is running"}
