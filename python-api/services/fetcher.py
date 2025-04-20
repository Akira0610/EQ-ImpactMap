# python-api/services/fetcher.py
import json
import os

def load_earthquake_data():
    try:
        # 根據你的資料夾位置修正路徑：
        file_path = os.path.abspath("../java-fetcher/out/usgs_data.json")
        
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] 無法載入地震資料: {e}")
        raise  # 把錯誤拋出，FastAPI 才能處理
            