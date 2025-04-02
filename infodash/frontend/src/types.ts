export interface WeatherData {
    name: string;
    main: {
      temp: number;
    };
}
  
export interface NewsData {
    articles: {
      title: string;
      url: string;
    }[];
}
  
export interface AppData {
    weather: WeatherData;
    news: NewsData;
}