import yfinance as yf
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from Packages import DataAccess

class Finance():
    def __init__(self):
        self.userlist = {}
        self.dal = DataAccess.dal()

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
        userwl = self.dal.get_user(user)
        result = {}
        for ticker in userwl['stocks'].keys():
            qoute = self.get_last_quote(ticker)
            sign = ''
            if qoute["changeDollar"] >= 0:
                sign = '+'
            result[userwl['stocks'][ticker]] = f'[{qoute["ticker"]}]     {qoute["currentPrice"]}     {sign}{qoute["changeDollar"]} ({sign}{qoute["changePercent"]}%)'
        return(result)
    def get_quote(self, ticker):
        ticker = str(ticker).upper()
        t = yf.Ticker(ticker)
        return(t)
    def add_userlist_item(self, user, ticker):
        ticker = str(ticker).upper()
        t = yf.Ticker(ticker)
        name = t.info['shortName']
        userwl = self.dal.get_user(user)
        if userwl is None:
            self.dal.add_user({
                                'userid': user,
                                'stocks': {ticker: name}
                            })
        else:
            if ticker in userwl['stocks']:
                return("Ticker already added!")
            else:
                userwl['stocks'][ticker] = name
                self.dal.upd_user(userwl)
            #self.userlist[user] = {ticker: name}
        return "Ticker added to your watchlist!"

    def del_userlist_item(self, user, ticker):
        ticker = str(ticker).upper()
        userwl = self.dal.get_user(user)
        userwl['stocks'].pop(ticker)
        self.dal.upd_user(userwl)
        return "Ticker removed from the list!"
    def get_last_quote(self, ticker):
        t = yf.Ticker(ticker)
        data = t.history(period="max", interval="1d").tail(2)
        beforeLastDay = data.iloc[0, :]
        lastDay = data.iloc[1, :]
        #last_quote = data.tail(1)
        closePrice = round(lastDay['Close'],2)
        previousClose = round(beforeLastDay['Close'],2)
        changeDollar = round(closePrice - previousClose,2)
        changePercent = round((changeDollar/previousClose)*100,2)
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



        
