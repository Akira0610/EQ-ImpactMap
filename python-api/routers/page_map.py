# ✅ python-api/routers/page_map.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from .earthquake import get_earthquakes

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# ✅ GET /map：回傳 map.html 給使用者
@router.get("/map", response_class=HTMLResponse)
def render_template_map(request: Request):
    # data = load_earthquake_data()
    # html = generate_earthquake_map(data)
    return templates.TemplateResponse("map.html", {
        "request": request,
    })


# ✅ POST /earthquake-info：接收查詢條件並回傳地震的資料
@router.post("/earthquake-info", response_class=JSONResponse)
async def render_dynamic_map(request: Request):
    try:
        filterpara = await request.json()
        result1 = get_earthquakes(
            min_magnitude=filterpara.get("min_magnitude"),
            max_magnitude=filterpara.get("max_magnitude"),
            start_time=filterpara.get("start_time"),
            end_time=filterpara.get("end_time"),
            region=filterpara.get("region")
        )
        # html = generate_earthquake_map(result1)
        return JSONResponse(content=result1)
    except Exception as e:
        return JSONResponse(content=f"<h3>地圖產生失敗：{e}</h3>", status_code=500)

