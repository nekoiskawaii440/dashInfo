import os
import requests
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
#load_dotenv()  # .env ファイルを読み込む

def get_weather(city: str = "Tokyo"):
    api_key = os.getenv("API_KEY")  # 環境変数からAPIキーを取得
    if not api_key:
        return {"error": "API Key not found."}
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Failed to get weather data: {response.status_code}"}
    
    return response.json()