import schedule
import time
from services.usgs_fetcher import fetch_major_earthquakes
import json
import os

def update_data():
    print("🔁 更新 USGS 地震資料...")
    data = fetch_major_earthquakes(start_time="2024-01-01", min_magnitude=4.0)
    save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../java-fetcher/out/usgs_data.json"))
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump({
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["longitude"], d["latitude"]]
                },
                "properties": {
                    "place": d["place"],
                    "mag": d["magnitude"],
                    "time": d["time"]
                }
            } for d in data]
        }, f, ensure_ascii=False, indent=2)
    print("✅ 更新完成")

# 每 10 分鐘跑一次（可改成你要的頻率）
schedule.every(10).minutes.do(update_data)

if __name__ == "__main__":
    print("⏳ 啟動自動地震資料更新任務...")
    update_data()  # 啟動時先跑一次
    while True:
        schedule.run_pending()
        time.sleep(1)
