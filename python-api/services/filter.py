# services/filter.py

from datetime import datetime

def filter_earthquakes(data, min_mag=None, max_mag=None, start_time=None, end_time=None, region=None):
    filtered = []

    for feature in data.get("features", []):
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]

        # 條件
        mag = props.get("mag", 0)
        time = props.get("time")  # epoch time
        place = props.get("place", "")

        # 時間轉換
        event_time = datetime.utcfromtimestamp(time / 1000)

        # 條件過濾
        if min_mag is not None and mag < min_mag:
            continue
        if max_mag is not None and mag > max_mag:
            continue
        if start_time:
            start_dt = datetime.fromisoformat(start_time)
            if event_time < start_dt:
                continue
        if end_time:
            end_dt = datetime.fromisoformat(end_time)
            if event_time > end_dt:
                continue
        if region and region.lower() not in place.lower():
            continue

        filtered.append({
            "place": place,
            "magnitude": mag,
            "time": event_time.isoformat(),
            "coordinates": coords
        })

    return filtered
