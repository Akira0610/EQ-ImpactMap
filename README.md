# Global Earthquake Realtime Visualization Platform
![Language](https://img.shields.io/badge/language-python-blue)
![Language](https://img.shields.io/badge/language-JavaScript-yellow)
![Language](https://img.shields.io/badge/language-JAVA-orangered)
![Language](https://img.shields.io/badge/language-CSS-purple)
![Language](https://img.shields.io/badge/language-HTML-brown)
![License](https://img.shields.io/badge/language-dockerfile-lightblue)

👉 [🌐 Click here to try the live demo](https://eqidv-back-latest.onrender.com/map)  
(P.S. This is a free-tier deployment, so the site may sleep when idle)

# 🌏Table of Contents 
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [License](#license)
- [Acknowledgements](#acknowledgements)

  
## Introduction
The Global Earthquake Realtime Visualization Platform is a full-stack web application that fetches real-time earthquake data from the USGS and displays it visually on an interactive world map. The goal is to help users quickly understand the location, magnitude, and impact of earthquakes.
### Data Source: USGS Earthquake Catalog  

## Installation
1. install Dependencies
```
pip install -r requirements.txt
```
2. Compile and Run Java Fetcher
- Compile the Java program:
  ```javac -d out src/EarthquakeFetcher.java```
- Run the fetcher:
  ```java -cp out EarthquakeFetcher```
3. Start Python API Server
```
cd python-api
uvicorn main:app --reload
```
4. Open your browser <http://localhost:8000/map>

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
  - FastAPI Router route `page_map.py` handles `/map` requests.  
### Earthquake Data Fetching
  - Java service periodically pulls the latest data from the USGS feed.
  - Data is pre‑processed and stored for the API. 
### API Services
  - **FastAPI (Python)** –  provides a RESTful API(/earthquakes) returning JSON.
  - Main routers`earthquake.py`.  
### Map Rendering and Interaction
  - Pydeck + Mapbox visualise earthquakes as markers.
  - Tooltips reveal magnitude, depth, location, and UTC timestamp. 
### Frontend Interactionand Search
  - `main.js` handles the search form, client‑side validation, and API calls.
  - User queries trigger map refreshes with filtered data.    

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
***This project is intended for personal learning and portfolio demonstration only. Unauthorized commercial use is prohibited.***

## Acknowledgements 
Thank you for checking out my FIRST project!  
Feel free to open an issue if you have any questions or suggestions.
Feel free to open issue if you have any suggestions or questions.
  
`Special thanks to my best friend KCL and OuO.`
