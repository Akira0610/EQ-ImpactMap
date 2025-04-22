from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.map_renderer import generate_earthquake_map
from services.fetcher import load_earthquake_data

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/map")
def render_map(request: Request):
    data = load_earthquake_data()
    html = generate_earthquake_map(data)
    return templates.TemplateResponse("map.html", {
        "request": request,
        "deck_html": html
    })
