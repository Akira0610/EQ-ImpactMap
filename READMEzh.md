  # Global Earthquake Realtime Visualization Platform
![Language](https://img.shields.io/badge/language-python-blue)
![Language](https://img.shields.io/badge/language-JS-yellow)
![Language](https://img.shields.io/badge/language-JAVA-red)
![Language](https://img.shields.io/badge/language-CSS-purple)
![Language](https://img.shields.io/badge/language-HTML-brown)
![License](https://img.shields.io/badge/license-yes-yellow)

# 🌏目錄
- [簡介](#專案簡介)
- [安裝方式](#安裝方式)
- [功能清單](#功能清單)
- [技術架構](#技術架構)
- [系統架構圖](#系統架構圖)
- [授權條款](#授權條款)
- [規劃](#規劃)
- [銘謝](#銘謝)
  
## 簡介 | Introduction
一個即時整合 USGS 全球地震資料的互動式地圖平台，使用 FastAPI + Pydeck + Mapbox 實作，支援地震篩選、地圖即時更新，並提供搜尋與視覺化功能。  


### 資料來源：美國地質調查局資料庫

## 安裝方式
1. 安裝需要的要件
```
pip install -r requirements.txt
```
3. 啟動伺服器
```
cd python-api
uvicorn main:app --reload
```
3. 開始瀏覽器
瀏覽 http://localhost:8000/map 即可開始使用。

## 功能清單
- 即時獲取全球地震資料
- 支援搜尋（震度、時間、地區）
- 動態更新地圖
- 地震點顯示詳細資訊
- 支援縮放、拖曳、互動

## 技術架構
### 使用者
  - 使用者透過瀏覽器訪問網站。
  - 後端提供靜態檔案(HTML,JavaScript,CSS)給前端載入。
  - FastAPI路由 `page_map.py /map`負責傳回`/map`頁面。  
### 地震資料抓取
  - 後端使用JAVA定時從USGS抓取最新地震資料。
  - 資料經過初步處理存入後端資料夾。
  - 主要程式 : `java-fetcher`。
### API服務
  - **FastAPI (Python)** – 提供地震資料的 RESTful API
  - 支援篩選條件(時間、規模、地區)，並回傳JSON資料。
  - 主要API : `earthquake.py`,路由`earthquakes`。  
### 地圖渲染與互動
  - 使用Pydeck和Mapbox將地震資料視覺化成地圖紅點。
  - 地圖支援紅點顯示tooltip地震詳細資訊
  - 地圖生成 : `map_generator.py`
### 前端互動與搜尋
  - 前端JS負責處理搜尋表單及防呆驗證。
  - 使用者輸入篩選條件，前端呼叫後端API更新地圖資料
  - 主要程式: `main.js`  
### 定時更新與資料同步
  - ?

---
## 系統架構圖

```
[美國地質調查局] 
   ↓  (抓取資料)
[Java 抓取資料]
   ↓  (處理並傳送)
[FastAPI 服務 (Python)]
   ↓  (提供API端點)
[前端 (HTML / JS)]
   ↓  (顯示)
[Deck.gl + Mapbox Interactive Map]
```
## 授權條款
此專案僅供個人學習與履歷展示用途，禁止未經授權之商業用途。  

## 規劃
- 切換至 React 前端
- 多語言支援（如繁體中文/英文）
- 隨著MW變化有不同顏色的球
- 對於重大地震有個新聞的超連結 附註在tooltip下方
- 丟去伺服器
- 響應式網頁

## 銘謝
感謝您使用/閱覽我人生中第一個專案!!如果有任何建議或問題，歡迎提出Issue。  
