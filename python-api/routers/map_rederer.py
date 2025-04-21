from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
import pandas as pd
import pydeck as pdk
import os
import json

router = APIRouter()

@router.get("/map", response_class=HTMLResponse)
def render_map(min_magnitude: float = Query(0.0)):
    # 讀取 JSON 檔（假設是 usgs_data.json）
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "usgs_data.json")
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except Exception as e:
        return f"無法讀取資料：{str(e)}"

    # 將 json 轉成 DataFrame 並篩選
    records = raw_data.get("features", [])
    data = []
    for r in records:
        props = r["properties"]
        coords = r["geometry"]["coordinates"]
        if props["mag"] is not None and props["mag"] >= min_magnitude:
            data.append({
                "lon": coords[0],
                "lat": coords[1],
                "magnitude": props["mag"],
                "place": props["place"]
            })
    df = pd.DataFrame(data)

    if df.empty:
        return "找不到符合條件的地震資料"

    # 建立 Pydeck 圖層
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[lon, lat]",
        get_radius="magnitude * 10000",
        get_color="[255, 0, 0, 160]",
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=df["lat"].mean(),
        longitude=df["lon"].mean(),
        zoom=2
    )

    deck = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{place}\nMagnitude: {magnitude}"})

    return deck.to_html(as_string=True)
