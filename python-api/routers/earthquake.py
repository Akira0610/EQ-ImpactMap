# ✅ python-api/routers/earthquake.py

from fastapi import APIRouter, Query
from services.fetcher import load_earthquake_data
from services.filter import filter_earthquakes
from typing import Optional

router = APIRouter()


def get_earthquakes(
    min_magnitude: Optional[float],
    max_magnitude: Optional[float],
    start_time: Optional[str],
    end_time: Optional[str],
    region: Optional[str],
):
    try:
        min_magnitude = float(min_magnitude) if min_magnitude not in (None, "", "null") else None
        max_magnitude = float(max_magnitude) if max_magnitude not in (None, "", "null") else None
        start_time = start_time if start_time not in (None, "", "null") else None
        end_time = end_time if end_time not in (None, "", "null") else None
        region = region if region not in (None, "", "null") else None

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
    
    except Exception as e:
        return {"error": f"發生錯誤：{str(e)}"}
