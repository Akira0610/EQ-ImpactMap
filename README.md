  # Global Earthquake Realtime Visualization Platform
  ## 全球地震實時視覺化平台

![License](https://img.shields.io/badge/license-yes-yellow)
![Language](https://img.shields.io/badge/language-c++-brightgreen)
![Language](https://img.shields.io/badge/language-JAVA-red)
![Language](https://img.shields.io/badge/language-python-blue)  
🌏 
- [簡介 | Itroduction](#專案簡介--introduction)
- [安裝方式 | Installation](#安裝方式--installation)
- [功能清單 | Usage](#功能清單--usage)
- [技術架構 | Tech Stack](#技術架構--techstack)
- [授權條款 | License](#授權條款--license)
- [規劃 | Todo](#規劃--todo)
  
## 簡介 | Introduction
一個即時整合 USGS 全球地震資料的互動式地圖平台，使用 FastAPI + Pydeck + Mapbox 實作，支援地震篩選、地圖即時更新，並提供搜尋與視覺化功能。  
An interactive real-time earthquake data visualization platform, bulit with FastAPI,Pydeck,and Mapbox.  
### 資料來源：美國地質調查局資料庫 ( Data Sources : USGS Earthquake Database )

## 安裝方式 | Installation
1. 安裝需要的要件 | install requirements
```
pip install -r requirements.txt
```
3. 啟動伺服器 | Start the backend server
```
cd python-api
uvicorn main:app --reload
```
3. 開始瀏覽器 | Open youe browser and go to
瀏覽 http://localhost:8000/map 即可開始使用。

## 功能清單 | Usage
- 即時獲取全球地震資料 | Instantly retrieve global earthquake data
- 支援搜尋（震度、時間、地區） | Support searching (magnitude, time, location)
- 動態更新地圖 | Dynamically update the map
- 地震點顯示詳細資訊 | Display detailed information on map points
- 支援縮放、拖曳、互動 | Zooming, dragging, and navigation support

## 技術架構 | Tech Stack
1. 使用者(瀏覽者) 逛網頁
    後端提供靜態檔案 (html, js, css) 給瀏覽者
    `page_map.py GET /map`
### 後端 | Backend
- **FastAPI (Python)** – 提供地震資料的 RESTful API
- **Java** – 從 USGS 抓取並預處理即時地震資料

### 前端 | Frontend
- **HTML / CSS / JavaScript** – 使用者介面建置
- **Deck.gl + Mapbox** – 互動式地圖視覺化

### 資料來源 | Data Source
- **USGS (United States Geological Survey)** – 全球即時地震資料

### 地圖框架 | Map Framework
- **Pydeck** – 基於 Deck.gl 的 Python 視覺化工具

### 部署環境 (選填) | Deployment (Optional)
- **Localhost**（本地開發測試）
- （可日後補上雲端部署平台如 Vercel、AWS）

---

## 系統架構圖 | System Architecture

```
plaintext
[USGS] 
   ↓  (Fetch data)
[Java Fetcher]
   ↓  (Process and send)
[FastAPI Server (Python)]
   ↓  (Provide API endpoints)
[Frontend (HTML / JS)]
   ↓  (Display)
[Deck.gl + Mapbox Interactive Map]
```
## 授權條款 | License  
此專案僅供個人學習與履歷展示用途，禁止未經授權之商業用途。  
This project is intended for personal learning and portfolio demonstration only. Unauthorized commercial use is prohibited.

## 規劃 | Todo
1. 切換至 React 前端
2. 增加地震動畫回放功能
3. 手機版介面最佳化
4. 多語言支援（如繁體中文/英文）
5. 隨著MW變化有不同顏色的球
6. 對於重大地震有個新聞的超連結 附註在tooltip下方
7. deploy to sever
8. if we can finish, use RWD(Responsive Web Design)


