# 全球地震實時視覺化平台 | Global Earthquake Realtime Visualization Platform


# 專案簡介(Project Introduction)
一個即時整合 USGS 全球地震資料的互動式地圖平台，使用 FastAPI + Pydeck + Mapbox 實作，支援地震篩選、地圖即時更新，並提供搜尋與視覺化功能。
An interactive real-time earthquake data visualization platform, bulit with FastAPI,Pydeck,and Mapbox.

資料來源：美國地質調查局資料庫
Data Sources : USGS Earthquake Database

# 安裝方式 | Installation
1. 安裝需要的要件 (install requirements)
`pip install -r requirements.txt`
2. 啟動伺服器 (Start the backend server)
`cd python-api
uvicorn main:app --reload`
3. 開始瀏覽器 | Open youe browser and go to :
瀏覽 http://localhost:8000/map 即可開始使用。

# 功能特色(Features)
🔍 功能特色
1. 即時獲取全球地震資料
2. 支援搜尋（震度、時間、地區）
3. 動態更新地圖
4. 點擊地震點顯示詳細資訊
5. 前端表單防呆機制
6. 地圖美觀且支援縮放、拖曳、互動

# 主要模組說明(Main module description)
模組 | 說明
main.py | FastAPI 主入口，註冊路由與靜態檔案設定
routers/earthquake.py | 地震資料查詢 API
routers/page_map.py | 地圖頁面渲染 API
services/usgs_fetcher.py | 即時擷取 USGS 地震資料
services/filter.py | 資料篩選邏輯
services/map_generator.py | 產生 Pydeck 地圖 HTML
templates/map.html | 地圖頁面模板
static/js/main.js | 前端互動與防呆邏輯
static/css/style.css | 頁面樣式設定

# 規劃(TODO)
1.  切換至 React 前端
2. 增加地震動畫回放功能
3. 手機版介面最佳化
4. 多語言支援（如繁體中文/英文）


# 架構

1. 使用者(瀏覽者) 逛網頁
    後端提供靜態檔案 (html, js, css) 給瀏覽者
    `page_map.py GET /map`
