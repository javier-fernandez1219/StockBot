import yfinance as yf
import pandas as pd
import bs4
import requests
from bs4 import BeautifulSoup
from yfinance import ticker
class Finance():
    def __init__(self):
        self.userlist = {}

    def get_ticker(self, ticker):
        #print(self.test)
        print(f'Ticker {ticker} Info:\n')
        t = yf.Ticker(ticker)
        return t.history(period="max").tail()

    def get_dividend(self, ticker):
        print(f'Divident for ticker {ticker} not implemented.')
        d = yf.ticker(ticker)
        return d.dividens.tail(1)

    # def parsePrice():
    #     tickerSymbol = 'FB'
    #     r =requests.get('https://finance.yahoo.com/quote/'+{tickerSymbol}+'/='+{tickerSymbol})
    #     soup = bs4.BeautifulSoup(r.text,"xml")
    #     price=soup.find_all('div',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].find('span').text
    #     return price
    # while True:
    #     print('the current price: '+str(parsePrice()))


    