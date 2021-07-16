import yfinance as yf
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from yfinance import ticker

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
        return(self.userlist[user])

    def add_userlist_item(self, user, ticker):
        if user in self.userlist.keys():
            list = self.userlist[user]
            if ticker in list:
                return("Ticker already added!")
            else:
                list.append(ticker.upper()) 
        else:
            self.userlist[user]=[ticker.upper()]
        return "Ticker added to your watchlist!"

    def del_userlist_item(self, user, ticker):
        list = self.userlist[user]
        list.remove(ticker.upper())
        return "Ticker removed from the list!"

def getData(symbol):
    url=f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    'symbol': symbol,
    'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

print(getData('TSLA'))  


     
