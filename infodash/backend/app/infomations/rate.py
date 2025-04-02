import yfinance

def get_rate():
    tickerUS = "USDJPY=X"
    rateUS = yfinance.Ticker(tickerUS).history(period="1d").Close[0]
    tickerEU = "EURJPY=X"
    rateEU = yfinance.Ticker(tickerEU).history(period="1d").Close[0]
    tickerCN = "CNYJPY=X"
    rateCN = yfinance.Ticker(tickerCN).history(period="1d").Close[0]

    tickerNikkei = "^N225"
    Nikkei = yfinance.Ticker(tickerNikkei).history(period="1d").Close[0]
    tickerDow30 = "^DJI"
    Dow30 = yfinance.Ticker(tickerDow30).history(period="1d").Close[0]
    tickerSP = "^GSPC"
    SP500 = yfinance.Ticker(tickerSP).history(period="1d").Close[0]
    tickerNASDAQ = "^IXIC"
    NASDAQ = yfinance.Ticker(tickerNASDAQ).history(period="1d").Close[0]
    return {
        "rateUS": rateUS,
        "rateEU": rateEU,
        "rateCN": rateCN,
        "Nikkei":Nikkei,
        "Dow30":Dow30,
        "SP500":SP500,
        "NASDAQ":NASDAQ,
    }