import pydeck as pdk
import pandas as pd
from datetime import datetime

def generate_earthquake_map(data) -> str:
    parsed = []

    # ✅ USGS 原始格式（GeoJSON）
    if isinstance(data, dict) and "features" in data and isinstance(data["features"], list):
        features = data["features"]
        for r in features:
            props = r.get("properties", {})
            coords = r.get("geometry", {}).get("coordinates", [])
            if len(coords) >= 2:
                try:
                    parsed.append({
                        "lon": float(coords[0]),
                        "lat": float(coords[1]),
                        "depth": float(coords[2]) if len(coords) > 2 else 0,
                        "magnitude": float(props.get("mag", 0)),
                        "place": props.get("place", "Unknown"),
                        "time": datetime.utcfromtimestamp(props["time"] / 1000).strftime("%Y-%m-%d %H:%M UTC")
                    })
                except Exception:
                    continue

    # ✅ 已處理過的 FastAPI 格式
    elif isinstance(data, dict) and "features" in data and isinstance(data["features"], list):
        for r in data["features"]:
            coords = r.get("coordinates", [])
            if len(coords) >= 2:
                try:
                    parsed.append({
                        "lon": float(coords[0]),
                        "lat": float(coords[1]),
                        "depth": float(coords[2]) if len(coords) > 2 else 0,
                        "magnitude": float(r.get("magnitude", 0)),
                        "place": r.get("place", "Unknown"),
                        "time": datetime.fromisoformat(r["time"]).strftime("%Y-%m-%d %H:%M UTC")
                    })
                except Exception:
                    continue

    # ✅ 已完全處理過的 List 格式
    elif isinstance(data, list):
        parsed = data

    else:
        return "<h3>❌ 地圖產生失敗：資料格式錯誤</h3>"

    # ✅ 若資料為空
    if not parsed:
        return "<h3>❌ 找不到符合條件的地震資料</h3>"

    df = pd.DataFrame(parsed)

    # ✅ 確認欄位完整性
    if df.empty or "lon" not in df or "lat" not in df:
        return "<h3>❌ 無有效的地震位置資料</h3>"

    # ✅ Pydeck Layer 設定
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position="[lon, lat]",
        get_radius="magnitude * 8000",
        get_color="[255, 0, 0, 140]",
        pickable=True
    )

    view_state = pdk.ViewState(
        longitude=df["lon"].mean(),
        latitude=df["lat"].mean(),
        zoom=2,
        pitch=45
    )

    # ✅ Mapbox + Tooltip
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
        tooltip={
            "html": """
                <div>
                    <b>{place}</b><br/>
                    Magnitude: {magnitude}<br/>
                    Depth: {depth} km<br/>
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
