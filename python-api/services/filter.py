from datetime import datetime

def filter_earthquakes(data, min_mag=None, max_mag=None, start_time=None, end_time=None, region=None):
    if not data or "features" not in data:
        print("[ERROR] 地震資料為空或格式錯誤")
        return {"features": []}

    filtered = []
    for eq in data["features"]:
        props = eq["properties"]
        coords = eq["geometry"]["coordinates"]
        time_utc = datetime.utcfromtimestamp(props["time"] / 1000)

        # ✅ 條件篩選
        if min_mag is not None and props.get("mag", 0) < min_mag:
            continue
        if max_mag is not None and props.get("mag", 0) > max_mag:
            continue
        if start_time:
            try:
                if time_utc < datetime.fromisoformat(start_time):
                    continue
            except:
                print("[WARNING] start_time 格式錯誤，已略過")
        if end_time:
            try:
                if time_utc > datetime.fromisoformat(end_time):
                    continue
            except:
                print("[WARNING] end_time 格式錯誤，已略過")
        if region and region.lower() not in props.get("place", "").lower():
            continue

        # ✅ 符合條件者加入
        filtered.append({
            "place": props.get("place", "Unknown"),
            "magnitude": props.get("mag", 0),
            "time": time_utc.isoformat(),
            "coordinates": coords
        })

    print(f"[DEBUG] ✅ 過濾後筆數: {len(filtered)}")
    return filtered