import json
import os


def load_earthquake_data():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../java-fetcher/out/usgs_data.json"))
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] 無法載入地震資料: {e}")
        raise