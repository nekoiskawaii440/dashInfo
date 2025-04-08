# Infodash

リポジトリ作成時に名前間違えた...

## 本アプリについて
ダッシュボードアプリです。  
ひと目で情報がわかるようにダッシュボード形式のアプリを作成しようと思い作成しました。  
現段階では取得時の時刻、天気、為替情報、株価の平均、ニュースタイトルがわかるようになっています。  

## 実行時の注意
・infodash/backend/app直下に.envファイルが必要。  
  　ファイルの中身は天気情報を取得するためのAPIキーの記述をする。  
  　今回はOpenWeatherAPIを使用しています。  
```.env:.env
API_KEY=hogehogehoge
```
## 実行手順
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
cd frontend
npm install
npm start
```
