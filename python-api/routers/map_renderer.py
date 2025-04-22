from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.map_renderer import generate_earthquake_map
from services.fetcher import load_earthquake_data
from services.filter import filter_earthquakes

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/map", response_class=HTMLResponse)
def render_map(request: Request):
    data = load_earthquake_data()
    html = generate_earthquake_map(data)
    return templates.TemplateResponse("map.html", {"request": request, "deck_html": html})


# ✅ 新增此 POST 端點（從 JS 動態更新地圖）
@router.post("/map", response_class=HTMLResponse)
async def update_map_post(data: dict):
    filtered = filter_earthquakes(
        data,
        min_mag=None,  # 如果你有前端條件可自行擴充
    )
    html = generate_earthquake_map({"features": filtered})
    return HTMLResponse(content=html)
