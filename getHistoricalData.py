# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:16:31 2020

@author: walte

This program pulls the historical data for multiple tickers based on a txt file.

"""

import os.path
from os import path
import pandas as pd
from colors import red, green, blue
from pyfinmod import basic
from yahoofinancials import YahooFinancials
import datetime

path="D:/wdolan_stuff/PythonCode/"

# Get todays date and format correctly for get_historical_data later
today = datetime.date.today()
t=str(today.year) + '-' + str(today.month) + '-' + str(today.day)
print(t)
yesterday = today - datetime.timedelta(days=1)
y = str(yesterday.year) + '-' + str(yesterday.month) + '-' + str(yesterday.day)
print(y)
# open file a read contents to a list
f = open(str(path) +  'StockList.txt.txt')
try:
    tickers = list(f)
finally:
    f.close()
# iterate list of tickers 
for ticker in tickers:
    ticker = ticker.rstrip("\n")
    print('Ticker: ' + ticker) 

    #tsla_df.head()p

    
    ticker_path= (str(path) + str(ticker) + '.csv')
    if os.path.exists(ticker_path):
        print ("File exist")
    else:
        print ("File does not exist pulling all historical data")
        yahoo_financials = YahooFinancials(ticker)
        yahoo_financials.get_stock_price_data(reformat=True)
        data = yahoo_financials.get_historical_price_data(start_date='1900-01-01',
                                        end_date=t,
                                        time_interval='daily')
        tsla_df = pd.DataFrame(data[ticker]['prices'])
        tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
        tsla_df.to_csv(ticker_path,header=True)
        tsla_df['close'][135]
        len(tsla_df)