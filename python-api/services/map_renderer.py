import pydeck as pdk
import pandas as pd
from datetime import datetime

def generate_earthquake_map(data: dict) -> str:
    records = data.get("features", [])
    parsed = []
    for r in records:
        props = r["properties"]
        coords = r["geometry"]["coordinates"]
        if props.get("mag") is not None:
            parsed.append({
                "lon": coords[0],
                "lat": coords[1],
                "magnitude": props["mag"],
                "place": props.get("place", ""),
                "time":datetime.utcfromtimestamp(props["time"] / 1000).strftime("%Y-%m-%d %H:%M UTC")
            })
    df = pd.DataFrame(parsed)

    if df.empty:
        return "<h3>No earthquake data found.</h3>"

    layer = pdk.Layer(  # ⬅ 這一定要有
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

