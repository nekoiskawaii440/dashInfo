import React, { useState, useEffect } from 'react';
import './App.css';
import { fetchData } from "./service/api";
import { AppData } from './types';

function NewsList({ news }: { news: string[] }) {
  return (
    <ul>
      {news.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}

function App() {
  const [data, setData] = useState<{ weather: any; news: any; current_time: any, rate: any} | null>(null);

  useEffect(() => {
    fetchData("Tokyo")
      .then(setData)
      .catch((error) => {
        console.error("Error fetching data:", error);
        // エラーハンドリングのために適切な状態を設定
        setData(null);
      });
  }, []);

  return (
    <div>
      <div className="title">
        <h1>InfoDash</h1>
      </div>
      <div className="wrap">
        <div className="leftside">
          <div className='time-wrap'>
            <div className='box'>
              <h2>情報取得時刻</h2>
              {data?.current_time ? (
                <div className="time">
                  <p>{data?.current_time}</p>
                </div>
              ): (
              <p>Loading time...</p>
              )
              }
            </div> 
          </div>
          <div className="contents1">
            <div className="box">
              <h2>天気情報</h2>
              {data?.weather ? (
                <div  className="card weather">
                  <h3 className="city">{data.weather.name}</h3>
                  <p className="temp">🌡️ {data.weather.main.temp}°C</p>
                  <img
                    src={`https://openweathermap.org/img/wn/${data.weather.weather[0].icon}@2x.png`}
                    alt="Weather icon"
                    className="icon"
                  />
                  <p className="condition">🌥️ {data.weather.weather[0].description}</p>
                </div>
              ) : (
                <p>Loading weather...</p>
              )}
            </div>
            
            <div className="box">
              <h2>ニュース</h2>
              {data?.news ? (
                <div  className="card">
                  <NewsList news={data.news?.news} />
                </div>
              ) : (
                <p>Loading news...</p>
              )}
            </div>
          </div>
        </div>
        <div className="rightside">
          <div className='contents2'>
            <div className="box">
              <h2>為替レート</h2>
              {data?.rate ? (
                <div  className="card">
                  <p>米(ドル) / 日本(円): {data.rate?.rateUS}</p>
                  <p>欧州(ユーロ) / 日本(円): {data.rate?.rateEU} </p>
                  <p>中国(元) / 日本(円): {data.rate?.rateCN}</p>
                </div>
              ) : (
                <p>Loading rate...</p>
              )}
            </div>
            <div className="box">
              <h2>平均株価</h2>
              {data?.rate ?(
                <div className='card'>
                  <p>日経225 : {data.rate?.Nikkei}</p>
                  <p>Dow 30 : {data.rate?.Dow30}</p>
                  <p>S&P 500 : {data.rate?.SP500}</p>
                  <p>NASDAQ : {data.rate?.NASDAQ}</p>
                </div>
              ):(
                <p>Loading rate...</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
