# Imports
import datetime
import pandas as pd
import yfinance as yf
import yahoo_fin.stock_info as si


# Constants
TODAY = datetime.datetime.now()
WEEK_LOOKBACK = datetime.datetime.now() - datetime.timedelta(days=7)


def get_companies():
    """
    Description:

    This returns list of companies from sp500 including ticker
    and stock information.
    """
    stock_list = si.tickers_sp500(include_company_data=True)
    pd.set_option('display.max_rows', len(stock_list))
    return stock_list


def get_ticker(company_name):
    """
    Description:

    Use this to get ticker based on name

    Returns:

    Str ---> ticker
    """
    # collects list from top 500 companys
    stock_list = si.tickers_sp500(include_company_data=True)
    # filter out just company security and symbol
    df_list = stock_list.iloc[:, [0, 1]]
    # setting row return to length of data
    pd.set_option('display.max_rows', len(df_list))
    # searching secuirty col for row return
    company_ticker_serach = \
        df_list.loc[df_list['Security'].isin([company_name])]
    # setting cymbol to return var
    company_symbol = company_ticker_serach['Symbol'].values[0]
    # resetting row return to length of data
    pd.reset_option('display.max_rows')
    return company_symbol


def get_weeks_stock_data(company_symbol):
    """
    Description:

    Gets weeks worth of stock information for given stock name.

    Returns:
        Dataframe
    """
    # getting the previous weeks worth of data
    stock_price_data = yf.download(company_symbol, start=WEEK_LOOKBACK,
                                   end=TODAY, group_by='ticker', rounding=True,
                                   actions=True)
    return stock_price_data


def get_quote_table(ticker):
    """
    Description:

    This collects the quote table contents that has stock price
    dividend, PE ratio etc.

    Returns:
        Dict --> Stock informmation.

    """
    quote_table = si.get_quote_table(ticker)
    return quote_table


def get_dividends(qtable):
    # Gets Dividend and yield. Reuturns dividend.
    dividends = qtable['Forward Dividend & Yield'].split()
    div = dividends[0]
    return div


def get_pe_ratio(qtable):
    # Gets the Price earning ratio
    PE = qtable['PE Ratio (TTM)']
    return PE


def get_stock_price(qtable):
    # Gets stocks price
    stock_price = qtable['Quote Price']
    return round(stock_price, 2)


def get_ls_tickers():
    # returns list of tickers
    tickers = get_companies()
    return tickers.iloc[:, 0].tolist()

def get_ls_companies():
    # returns list of companies
    companies_name = get_companies()
    return companies_name.iloc[:, 1].tolist()
