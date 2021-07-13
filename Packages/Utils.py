import yfinance as yf
import pandas as pd

class Finance():
    def __init__(self):
        self.test = "test1"

    def get_ticker(self, ticker):
        #print(self.test)
        print(f'Ticker {ticker} Info:\n')
        t = yf.Ticker(ticker)
        return t.history(period="max").tail()

    def get_dividend(self, ticker):
        print(f'Divident for ticker {ticker} not implemented.')