# routers/earthquake.py

from fastapi import APIRouter
from typing import Optional
from services.fetcher import load_earthquake_data
from services.filter import filter_earthquakes

router = APIRouter()

@router.get("/")
def get_earthquakes(
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None,
    start_time: Optional[str] = None,  # 格式: YYYY-MM-DD
    end_time: Optional[str] = None,
    region: Optional[str] = None
):
    data = load_earthquake_data()
    if "error" in data:
        return data
    filtered = filter_earthquakes(data, min_magnitude, max_magnitude, start_time, end_time, region)
    return {
        "count": len(filtered),
        "earthquakes": filtered
    }
