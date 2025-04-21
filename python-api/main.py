from fastapi import FastAPI
from routers import earthquake

app = FastAPI()

# 註冊 earthqaukes 路由，處理地震查詢
app.include_router(earthquake.router, prefix="/earthquakes")

@app.get("/")
def root():
    return {"message": "API is up and running!"}
