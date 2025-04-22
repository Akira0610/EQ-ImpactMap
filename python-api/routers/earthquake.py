# ✅ 檔案位置：python-api/routers/earthquake.py

from fastapi import APIRouter, Query
from services.fetcher import load_earthquake_data
from services.filter import filter_earthquakes
from typing import Optional

router = APIRouter()

@router.get("/", tags=["Earthquakes"])
def get_earthquakes(
    min_magnitude: Optional[float] = Query(None),
    max_magnitude: Optional[float] = Query(None),
    start_time: Optional[str] = Query(None),
    end_time: Optional[str] = Query(None),
    region: Optional[str] = Query(None),
):
    raw_data = load_earthquake_data()
    filtered = filter_earthquakes(
        raw_data,
        min_mag=min_magnitude,
        max_mag=max_magnitude,
        start_time=start_time,
        end_time=end_time,
        region=region
    )
    return filtered
