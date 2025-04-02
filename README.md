# Infodash

リポジトリ作成時に名前間違えた...

## 本アプリについて
ダッシュボードアプリです。  
ひと目で情報がわかるようにダッシュボード形式のアプリを作成しようと思い作成しました。  
現段階では取得時の時刻、天気、為替情報、株価の平均、ニュースタイトルがわかるようになっています。  

## 実行時の注意
・infodash/backend/app直下に.envファイルが必要。
  ファイルの中身は天気情報を取得するためのAPIキーの記述をする。
  例）
```.env:.env
API_KEY=hogehogehoge
```
・pythonの仮想環境に下記ライブラリが必要
- yfinance
- load_dotenv
- BeautifulSoup
- FastAPI
- uvicorn
