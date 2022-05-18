# Imports
import datetime
import pandas as pd
import yfinance as yf 
import yahoo_fin.stock_info as si


# Constants
TODAY = datetime.datetime.now()
WEEK_LOOKBACK = datetime.datetime.now() - datetime.timedelta(days=7)


def get_companies():
    stock_list = si.tickers_sp500(include_company_data=True)
    pd.set_option('display.max_rows', len(stock_list))
    return stock_list

# Use this to get ticker based on name
# col 0 returns ticker symbol and col 1 company name
def get_ticker(company_name):
    
    # collects list from top 500 companys
    stock_list = si.tickers_sp500(include_company_data=True)
    # fileter out just company security and symbol
    df_list = stock_list.iloc[:, [0, 1]]
    # setting row return to length of data
    pd.set_option('display.max_rows', len(df_list))
    # searching secuirty col for row return
    company_ticker_serach = df_list.loc[df_list['Security'].isin([company_name])]
    # setting cymbol to return var
    company_symbol = company_ticker_serach['Symbol'].values[0]
    # resetting row return to length of data
    pd.reset_option('display.max_rows')
    return company_symbol

def get_weeks_stock_data(company_symbol):
    # getting the previous weeks worth of data
    stock_price_data = yf.download(company_symbol, start=WEEK_LOOKBACK,
                                   end=TODAY, group_by='ticker')
    return stock_price_data

