from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pydeck as pdk

app = FastAPI()

@app.get("/map", response_class=HTMLResponse)
def render_map():
    deck = pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=35.6895, longitude=139.6917, zoom=5, pitch=50),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=[{"position": [139.6917, 35.6895], "size": 100}],
                get_position="position",
                get_radius="size",
                get_color=[255, 0, 0],
                pickable=True
            )
        ]
    )
    return deck.to_html(as_string=True)
