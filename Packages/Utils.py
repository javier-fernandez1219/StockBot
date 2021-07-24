import yfinance as yf
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup

class Finance():
    def __init__(self):
        self.userlist = {}

    def get_ticker(self, ticker):
        #print(self.test)
        print(f'Ticker {ticker} Info:\n')
        t = yf.Ticker(ticker)
        return t.history(period="max")[["Open","High","Low","Close","Volume"]].tail(1)

    def get_dividend(self, ticker):
        print(f'Divident for ticker {ticker}.')
        d =yf.Ticker(ticker)
        return d.dividends.tail(1)
    
    def get_userlist(self, user):
        result = {}
        for ticker in self.userlist[user].keys():
            qoute = self.get_last_quote(ticker)
            result[self.userlist[user][ticker]] = f'({qoute["ticker"]})     {qoute["currentPrice"]}     {qoute["changeDollar"]} ({qoute["changePercent"]}%)'
        return(result)

    def add_userlist_item(self, user, ticker):
        t = yf.Ticker(ticker)
        name = t.info['shortName']
        if user in self.userlist.keys():
            list = self.userlist[user]
            if ticker in list.keys():
                return("Ticker already added!")
            else:
                list[ticker] = name
        else:
            self.userlist[user] = {ticker: name}
        return "Ticker added to your watchlist!"

    def del_userlist_item(self, user, ticker):
        self.userlist[user].remove(ticker)
        #self.userlist[user] = list(filter(lambda i: i['symbol'] != ticker.upper(), l))            
        return "Ticker removed from the list!"
    def get_last_quote(self, ticker):
        t = yf.Ticker(ticker)
        data = t.history(period="max", interval="1d").tail(2)
        beforeLastDay = data.iloc[0, :]
        lastDay = data.iloc[1, :]
        #last_quote = data.tail(1)
        closePrice = round(lastDay['Close'],3)
        previousClose = round(beforeLastDay['Close'],3)
        changeDollar = round(closePrice - previousClose,3)
        changePercent = round((changeDollar/previousClose)*100,3)
        qoute = {
            "ticker" : ticker,
            "currentPrice" : closePrice,
            "changeDollar" : changeDollar,
            "changePercent" : changePercent
        }
        return qoute

    def getData(self, symbol):
        url=f'https://finance.yahoo.com/quote/{symbol.upper()}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        stock = {
        'symbol': symbol,
        'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).findAll('span')[0].text,
        'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).findAll('span')[1].text,
        }
        return stock



        
