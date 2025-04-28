  # Global Earthquake Realtime Visualization Platform
![License](https://img.shields.io/badge/license-yes-yellow)
![Language](https://img.shields.io/badge/language-python,JAVA-blue)  

# 🌏目錄 | Table of Contents 
- [簡介 | Itroduction](#專案簡介--introduction)
- [安裝方式 | Installation](#安裝方式--installation)
- [功能清單 | Usage](#功能清單--usage)
- [技術架構 | Tech Stack](#技術架構--techstack)
- [系統架構圖 | System Architecture](#系統架構圖--systemarchitecture)
- [授權條款 | License](#授權條款--license)
- [規劃 | Todo](#規劃--todo)
- [銘謝 | Acknowledgements](#銘謝--acknowledgements)
  
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
### 使用者 | User
  - 使用者透過瀏覽器訪問網站。
  - 後端提供靜態檔案(HTML,JavaScript,CSS)給前端載入。
  - FastAPI路由 `page_map.py /map`負責傳回`/map`頁面。  
### 地震資料抓取 | Earthquake Data Fetching
  - 後端使用JAVA定時從USGS抓取最新地震資料。
  - 資料經過初步處理存入後端資料夾。
  - 主要程式 : `java-fetcher`。
### API服務 | API Services
  - **FastAPI (Python)** – 提供地震資料的 RESTful API
  - 支援篩選條件(時間、規模、地區)，並回傳JSON資料。
  - 主要API : `earthquake.py`,路由`earthquakes`。  
### 地圖渲染與互動 | Map Rendering and Interaction
  - 使用Pydeck和Mapbox將地震資料視覺化成地圖紅點。
  - 地圖支援紅點顯示tooltip地震詳細資訊
  - 地圖生成 : `map_generator.py`
### 前端互動與搜尋 | Fronted Interactionand Search
  - 前端JS負責處理搜尋表單及防呆驗證。
  - 使用者輸入篩選條件，前端呼叫後端API更新地圖資料
  - 主要程式: `main.js`  
### 定時更新與資料同步 | Scheduled Updates and Data Sync
  - ?

---
## 系統架構圖 | System Architecture

```
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
- 切換至 React 前端
- 多語言支援（如繁體中文/英文）
- 隨著MW變化有不同顏色的球
- 對於重大地震有個新聞的超連結 附註在tooltip下方
- deploy to sever
- if we can finish, use RWD(Responsive Web Design)

## 銘謝 | Acknowledgements 
感謝您使用/閱覽我人生中第一個專案!!如果有任何建議或問題，歡迎提出Issue。  
Thank you for using/watching my FIRST project!  
Feel free to open as issue if you have any suggestions or questions.
