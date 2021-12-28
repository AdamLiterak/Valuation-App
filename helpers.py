import yfinance as yf
import pandas as pd
from cs50 import SQL

def add(x,y):
    return (x+y)

def stock_screener(ticker_list):
    '''returns df with tickers and defined fundamentals'''
    info_list = []

    for i in ticker_list:
        info_list.append(yf.Ticker(i).info)

    # df = pd.DataFrame(info_list)
    # df = df.set_index('symbol')
    # df = df[df.columns[df.columns.isin(fundamentals_list)]]

    # return df
    return info_list

def ifnot(x):
    '''function returning text if non existent'''
    if not x:
        x = "-not found-"
    else:
        x = x

# GET DATA FUNCTIONS
def get_data_fmp(api_key,ticker,type,database):
    '''getting data from financial modeling prep and saving them into db,
    api_key from FMP, valid ticker, type = "PNL","BS" or "CF", database specified by name'''
    db = SQL("sqlite:///" + database)
    if type == "PNL":
        link = "https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=ed10beffd26075cd6e5178bae356ca27"
    elif type == "BS":
        link = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?limit=120&apikey=ed10beffd26075cd6e5178bae356ca27"
    elif type == "CF":
        link = "https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?limit=120&apikey=ed10beffd26075cd6e5178bae356ca27"
    else:
        pass