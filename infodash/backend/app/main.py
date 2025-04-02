import requests
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from infomations.weather import get_weather
from infomations.news import get_news
from infomations.rate import get_rate

app = FastAPI()

# CORS を許可するオリジンを設定
origins = [
    "http://localhost:3000",  # React アプリケーションの URL
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可する HTTP メソッド
    allow_headers=["*"],  # 許可するヘッダー
)

def get_current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now


@app.get("/", response_class=JSONResponse)
def root(city: str = "Tokyo"):
    weather_data = get_weather(city)
    news_data = get_news()
    currenttime_data = get_current_time()
    rate_data = get_rate()

    return JSONResponse (content={
        "weather": weather_data,
        "news": news_data,
        "current_time": currenttime_data,
        "rate": rate_data
    })