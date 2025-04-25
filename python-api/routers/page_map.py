# ✅ python-api/routers/page_map.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.fetcher import load_earthquake_data
from services.map_generator import generate_earthquake_map
import traceback

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ✅ GET /map：回傳 map.html + deck_html 給使用者
@router.get("/map", response_class=HTMLResponse)
def render_template_map(request: Request):
    data = load_earthquake_data()
    html = generate_earthquake_map(data)
    return templates.TemplateResponse("map.html", {
        "request": request,
        "deck_html": html
    })


# ✅ POST /map：接收查詢條件並更新地圖
@router.post("/map", response_class=HTMLResponse)
async def render_dynamic_map(request: Request):
    try:
        payload = await request.json()
        html = generate_earthquake_map(payload)
        return HTMLResponse(content=html)
    except Exception as e:
        return HTMLResponse(content=f"<h3>地圖產生失敗：{e}</h3>", status_code=500)

