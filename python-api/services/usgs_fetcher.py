# python-api/services/usgs_fetcher.py

import json
import requests
from datetime import datetime

def fetch_major_earthquakes(start_time="1900-01-01", min_magnitude=4.0, limit=500):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_time,
        "minmagnitude": min_magnitude,
        "orderby": "magnitude",
        "limit": limit,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"USGS API error: {response.status_code}")

    earthquakes = []
    data = response.json()

    for feature in data.get("features", []):
        properties = feature["properties"]
        geometry = feature["geometry"]

        if not geometry or not geometry.get("coordinates"):
            continue

        coordinates = geometry["coordinates"]
        earthquake = {
            "longitude": coordinates[0],
            "latitude": coordinates[1],
            "magnitude": properties.get("mag", 0),
            "place": properties.get("place", "Unknown"),
            "time": datetime.utcfromtimestamp(properties["time"] / 1000).isoformat()
        }
        earthquakes.append(earthquake)

    return earthquakes
