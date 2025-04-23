import pydeck as pdk
import pandas as pd
from datetime import datetime

def generate_earthquake_map(data) -> str:
    parsed = []

    # ✅ USGS 原始格式（帶 geometry 和 properties）
    if isinstance(data, dict) and "features" in data and isinstance(data["features"], list) and "properties" in data["features"][0]:
        for r in data["features"]:
            props = r["properties"]
            coords = r["geometry"]["coordinates"]
            parsed.append({
                "lon": coords[0],
                "lat": coords[1],
                "depth": coords[2],
                "magnitude": props.get("mag", 0),
                "place": props.get("place", ""),
                "time": datetime.utcfromtimestamp(props["time"] / 1000).strftime("%Y-%m-%d %H:%M UTC")
            })

    # ✅ FastAPI 回傳格式（features 是 dicts，每筆有 coordinates）
    elif isinstance(data, dict) and "features" in data and isinstance(data["features"], list):
        for r in data["features"]:
            coords = r.get("coordinates", [])
            if len(coords) >= 2:
                parsed.append({
                    "lon": coords[0],
                    "lat": coords[1],
                    "depth": coords[2] if len(coords) > 2 else 0,
                    "magnitude": r.get("magnitude", 0),
                    "place": r.get("place", ""),
                    "time": datetime.fromisoformat(r["time"]).strftime("%Y-%m-%d %H:%M UTC")
                })

    # ✅ 已完全處理過的 list
    elif isinstance(data, list):
        parsed.extend(data)

    else:
        return "<h3>⚠️ 地圖產生失敗：資料格式錯誤</h3>"

    print("[DEBUG] Parsed data preview:")
    print(parsed[:3])
    print("[DEBUG] Total parsed:", len(parsed))

    df = pd.DataFrame(parsed)
    print("[DEBUG] DataFrame columns:", df.columns)

    if df.empty:
        return "<h3>❌ 找不到任何符合條件的地震資料</h3>"

    # 🔴 這裡不要再拆 coordinates，因為已經拆過了
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[lon, lat]",
        get_radius="magnitude * 8000",
        get_color="[255, 0, 0, 160]",
        pickable=True
    )

    view_state = pdk.ViewState(
        longitude=df["lon"].mean(),
        latitude=df["lat"].mean(),
        zoom=2,
        pitch=45
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
        tooltip={
            "html": """
                <div>
                    <b>{place}</b><br/>
                    Magnitude: {magnitude}<br/>
                    Time: {time}
                </div>
            """,
            "style": {
                "backgroundColor": "white",
                "color": "black",
                "fontSize": "13px",
                "padding": "8px",
                "borderRadius": "6px"
            }
        }
    )

    return deck.to_html(as_string=True)
