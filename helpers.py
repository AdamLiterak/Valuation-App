import yfinance as yf
import pandas as pd

def add(x,y):
    return (x+y)

def stock_screener(ticker_list, fundamentals_list):
    '''returns df with tickers and defined fundamentals'''
    info_list = []

    for i in ticker_list:
        info_list.append(yf.Ticker(i).info)

    # df = pd.DataFrame(info_list)
    # df = df.set_index('symbol')
    # df = df[df.columns[df.columns.isin(fundamentals_list)]]

    # return df
    return info_list