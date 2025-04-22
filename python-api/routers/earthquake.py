# ✅ python-api/routers/earthquake.py

from fastapi import APIRouter, Query
from services.fetcher import load_earthquake_data
from services.filter import filter_earthquakes
from typing import Optional

router = APIRouter()

@router.get("")
def get_earthquakes(
    min_magnitude: Optional[str] = Query(default=None),
    max_magnitude: Optional[str] = Query(default=None),
    start_time: Optional[str] = Query(default=None),
    end_time: Optional[str] = Query(default=None),
    region: Optional[str] = Query(default=None),
):
    # ✅ 處理空字串轉換
    min_magnitude = float(min_magnitude) if min_magnitude else None
    max_magnitude = float(max_magnitude) if max_magnitude else None
    start_time = start_time or None
    end_time = end_time or None
    region = region or None

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
