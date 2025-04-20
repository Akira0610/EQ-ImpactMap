# python-api/services/map_renderer.py

import pydeck as pdk
import pandas as pd

def generate_earthquake_map(data: list[dict]) -> str:
    df = pd.DataFrame(data)

    # 建立地圖圖層
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position='[longitude, latitude]',
        get_color='[255, 0, 0, 140]',
        get_radius='magnitude * 10000',
        pickable=True
    )

    # 建立地圖視角
    view_state = pdk.ViewState(
        longitude=df["longitude"].mean() if not df.empty else 0,
        latitude=df["latitude"].mean() if not df.empty else 0,
        zoom=2,
        pitch=0
    )

    # 渲染成 HTML 字串
    deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
    return deck.to_html(as_string=True)
