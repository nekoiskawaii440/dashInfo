import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def get_news():
    data = None
    try:
        # ニュースのURL
        url = 'https://news.yahoo.co.jp/'
        data = requests.get(url)
        data.raise_for_status()
    except Exception as e:
        print(str(e))
        return {"news_list": ["読み込めませんでした"]}

    # HTMLを解析
    soup = BeautifulSoup(data.text, 'html.parser')

    # トピックセクションを探す
    topic_section = soup.find('section', class_='topics')

    # セクション内のすべてのリンクを取得
    news_links = topic_section.find_all('a')

    # トピックを取り出す
    topic_list = [link.get_text() for link in news_links]

    filtered_list = []
    for news_text in topic_list:
        if news_text == "もっと見る" or len(filtered_list) >= 8:
            break
        filtered_list.append(news_text)

    return {
        "news": filtered_list
    }