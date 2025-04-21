# routers/earthquake.py
from fastapi import APIRouter
import pydeck as pdk
from typing import Optional

router = APIRouter()

@router.get("/")
def get_earthquakes(
    min_magnitude: Optional[float] = None,
    max_magnitude: Optional[float] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    region: Optional[str] = None
):
    # 假設的地震數據（這裡應該替換為真實的數據）
    earthquake_data = [
        {"longitude": -122.4194, "latitude": 37.7749, "magnitude": 5.6},
        {"longitude": -118.2437, "latitude": 34.0522, "magnitude": 6.0},
        # 更多的地震數據...
    ]
    
    # 使用 pydeck 渲染地圖
    deck = pdk.Deck(
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=earthquake_data,
                get_position=["longitude", "latitude"],
                get_radius=10000,
                get_color=[255, 0, 0, 160],
                pickable=True,
            )
        ],
        initial_view_state=pdk.ViewState(
            latitude=37.7749,
            longitude=-122.4194,
            zoom=5,
            pitch=40.5,
        ),
    )
    
    # 返回渲染後的 HTML 內容
    return deck.to_html()

