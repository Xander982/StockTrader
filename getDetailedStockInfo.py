import yfinance as yf
import pandas as pd
from colors import red, green, blue
from pyfinmod import basic
from yahoofinancials import YahooFinancials
import datetime

path="D:/wdolan_stuff/PythonCode/"

# Get todays date and format correctly for get_historical_data later
today = datetime.date.today()
t=str(today.year) + '-' + str(today.month) + '-' + str(today.day)
# open file a read contents to a list
f = open(str(path) +  'StockList.txt.txt')
try:
    tickers = list(f)
finally:
    f.close()
# iterate list of tickers 
for ticker in tickers:
    ticker = ticker.rstrip("\n")
    #print('Enter ticker:')
    #ticker = input()
    print('Ticker: ' + ticker) 
    stock = yf.Ticker(ticker)
    yahoo_financials = YahooFinancials(ticker)
    yahoo_financials.get_stock_price_data(reformat=True)
    data = yahoo_financials.get_historical_price_data(start_date='2000-01-01',
                                    end_date=t,
                                    time_interval='daily')
    tsla_df = pd.DataFrame(data[ticker]['prices'])
    tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
    #tsla_df.head()
    tsla_df['close'][135]
    len(tsla_df)
    #json.load(open())
    
    ticker_path= (str(path) + str(ticker) + '.csv')
    
    tsla_df.to_csv(ticker_path,header=True)
    
    
    # get stock info;
    stock.info  
    
    bookValue= stock.info.get('bookValue')
    
    
    pegRatio= stock.info.get('pegRatio')
    
    EPS = stock.info.get('trailingEps')
    
    PERatio = stock.info.get('forwardPE')
    
    # Bright Red
    print('The P/E Ratio:(lower is better)     ',end =" ")
    print(u"\033[0;33;40m" + str(PERatio) + "\u001b[0m")
    
    #print(str(PERatio))
    print('The Book Value:                     ' + str(bookValue))
    print('Projected Earnings Growth:(<1 good) ' + str(pegRatio))
    print('Earnings/Share (higher is better)   ' + str(EPS))
    
    historical = yf.download(ticker, 
                          start='2020-07-02', 
                          end='2020-07-07', 
                          progress=False)
    
    hist = stock.history(period="max")