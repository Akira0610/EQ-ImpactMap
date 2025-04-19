# services/fetcher.py

import json

def load_earthquake_data(filepath="../../java-fetcher/out/usgs_data.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": f"無法讀取資料: {str(e)}"}
