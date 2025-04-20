# python-api/routers/earthquake.py

from fastapi import APIRouter
from typing import Optional
from services.fetcher import load_earthquake_data

router = APIRouter()

@router.get("/")
def get_earthquakes(
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    region: Optional[str] = None
):
    try:
        data = load_earthquake_data()
        # 可加入篩選邏輯
        return {
            "message": "資料載入成功",
            "filters": {
                "min_magnitude": min_magnitude,
                "max_magnitude": max_magnitude,
                "start_time": start_time,
                "end_time": end_time,
                "region": region
            },
            "results": data  # 現階段直接回傳所有資料
        }
    except Exception as e:
        return {"error": f"無法讀取資料: {str(e)}"}
