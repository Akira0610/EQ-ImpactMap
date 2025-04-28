# Global Earthquake Realtime Visualization Platform
![License](https://img.shields.io/badge/license-yes-yellow)
![Language](https://img.shields.io/badge/language-python,JAVA-blue)  

# 🌏Table of Contents 
- [Itroduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#techstack)
- [System Architecture](#systemarchitecture)
- [License](#license)
- [Todo](#todo)
- [Acknowledgements](#acknowledgements)
  
## Introduction
Global Earthquake Realtime Visualization Platform is an interactive web application that integrates real‑time earthquake data from the United States Geological Survey (USGS). Built with FastAPI, Pydeck, and Mapbox, the platform lets users filter earthquakes by magnitude, time, and region while exploring them on an interactive map that updates in real time.
Data Source: USGS Earthquake Catalog

## Installation
1. install requirements
```
pip install -r requirements.txt
```
2.Start the backend server
```
cd python-api
uvicorn main:app --reload
```
3.Open your browser and navigate to <http://localhost:8000/map>

## Usage
- Real‑time retrieval of global earthquake events
- Search by magnitude, time range, and location
- Dynamically updating deck.gl + Mapbox map
- Tooltips with detailed earthquake information
- Full map interaction (zoom, pan, rotate)

## Tech Stack
### Client
  - Users access the site with a standard web browser.
  - Static assets (HTML / JS / CSS) are served by FastAPI.
  - FastAPI Router `page_map.py /map`delivers the map page.`/map`.  
### 地震資料抓取 | Earthquake Data Fetching
  - Java service periodically pulls the latest data from the USGS feed.
  - Data are pre‑processed and stored for the API.
  - Main module: `java-fetcher`.  
### API Services
  - **FastAPI (Python)** –  provides a RESTful API(/earthquakes) returning JSON.
  - Main routers`earthquake.py`.  
### Map Rendering and Interaction
  - Pydeck + Mapbox visualise earthquakes as markers.
  - Tooltips reveal magnitude, depth, location, and UTC timestamp.
  - Map generation: `map_generator.py`  
### Fronted Interactionand Search
  - `main.js` handles the search form, client‑side validation, and API calls.
  - User queries trigger map refreshes with filtered data.  
### Scheduled Updates and Data Sync
  - ?

---
## System Architecture

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
## License  
This project is intended for personal learning and portfolio demonstration only. Unauthorized commercial use is prohibited.

## Todo
- Migrate front end to React
- Multi‑language support (English / Traditional Chinese)
- Colour‑coded markers based on magnitude
- Add news links for major earthquakes (shown in tooltips)
- deploy to sever
- Implement fully responsive design (RWD)

## Acknowledgements 
Thank you for checking out my FIRST project!  
Feel free to open an issue if you have any questions or suggestions.
Feel free to open as issue if you have any suggestions or questions.
