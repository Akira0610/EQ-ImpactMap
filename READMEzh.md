  # 全球即時視覺化地震平台
![Language](https://img.shields.io/badge/language-python-blue)
![Language](https://img.shields.io/badge/language-JavaScript-yellow)
![Language](https://img.shields.io/badge/language-JAVA-orangered)
![Language](https://img.shields.io/badge/language-CSS-purple)
![Language](https://img.shields.io/badge/language-HTML-brown)
![License](https://img.shields.io/badge/language-dockerfile-lightblue)

👉 [🌐 點我立即體驗線上版](https://eqidv-back-latest.onrender.com/map)  
(p.s.這是免費版所以網站會睡著)

# 🌏目錄
- [簡介](#簡介)
- [安裝方式](#安裝方式)
- [功能清單](#功能清單)
- [技術架構](#技術架構)
- [系統架構圖](#系統架構圖)
- [授權條款](#授權條款)
- [銘謝](#銘謝)

## 簡介
一個即時整合 USGS 全球地震資料的互動式地圖平台，使用 FastAPI + Pydeck + Mapbox ＋ ajax實作，支援地震篩選、地圖即時更新，並提供搜尋與視覺化功能。  
### 資料來源：美國地質調查局資料庫  
---  
## 安裝方式
1. 安裝需要的要件
- ```
  pip install -r requirements.txt
  ```
2. 編譯並啟動java抓取程式
- 編譯 Java 程式：
  ```
  javac -d out src/EarthquakeFetcher.java
  ```
- 啟動 Java 抓取程式：
  ```
  java -cp out EarthquakeFetcher
  ```
3. 啟動 Python API 伺服器
- ```
  cd python-api
  uvicorn main:app --reload
  ```
4. 開始瀏覽器
瀏覽 http://localhost:8000/map 即可開始使用。

##可以使用docker安裝環境

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
### API服務
  - **FastAPI (Python)** – 提供地震資料的 RESTful API
  - 支援篩選條件(時間、規模、地區)，並回傳JSON資料。
  - 主要API : `earthquake.py`,路由`earthquakes`。  
### 地圖渲染與互動
  - 使用Pydeck和Mapbox將地震資料視覺化成地圖紅點。
  - 地圖支援彩色點顯示tooltip地震詳細資訊
### 前端互動與搜尋
  - 前端JS(AJAX)負責處理搜尋表單及防呆驗證。
  - 使用者輸入篩選條件，前端呼叫後端API更新地圖資料
  - 主要程式: `main.js`  

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
[Deck.gl + Mapbox 地圖]
```
## 授權條款
此專案僅供個人學習與履歷展示用途，禁止未經授權之商業用途。  

## 銘謝
感謝您使用/閱覽我人生中第一個專案!!  
讓星星發光是我最大的動力~  
如果有任何建議或問題，歡迎提出Issue。  
感謝表情跟kcl
