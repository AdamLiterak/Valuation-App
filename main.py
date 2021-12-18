import re
from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
from cs50 import SQL
from helpers import add, stock_screener

# 1. download proper data on command into a database
# 2. view data from the database + add missing data manually
# 3. calculate the value of the company
# 4. print out the report inlcuding the value and the assumptions under the model.
# 5. addition: matrix with variances in value based on some changing input, chart showing some info about the stock

#export FLASK_APP=main.py
#q for exiting git commands in terminal
#token: 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

app = Flask(__name__)
db = SQL("sqlite:///data_1.db")

#reading a sql query file
file = open("query.sql")
queries = file.read()
file.close()
queries_list = queries.split(";")

#FUNCTIONS


#ROUTES
@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/model', methods=["GET","POST"])
def model():
  if request.method == "POST":
    ticker = request.form.get("ticker")
    pnl = db.execute(queries_list[0], ticker)
    columns = []
    for i in pnl[0]:
      columns.append(i)

    return render_template("model.html", columns=columns, pnl=pnl)

  else:
    return render_template("model.html")

@app.route('/valuation', methods=["GET", "POST"])
def valuation():

  if request.method == "POST":

    ticker = request.form.get("ticker")
    # ticker_list = [ticker]

    # discount_rate = request.form.get("discount_rate")

    #COMPANY DATA - rework this to use list of needed data 
    #info = stock_screener(ticker_list)

    #creating an yf onject
    ticker_yf = yf.Ticker(ticker)

    info = ticker_yf.info
    revenues = ticker_yf.earnings

    bs = ticker_yf.balance_sheet
    cf = ticker_yf.cashflow

    major_holders = ticker_yf.major_holders
    institutional_holders = ticker_yf.institutional_holders


    # company_details = info[0]['longBusinessSummary']
    # dividend_yield = float(info[0]['dividendYield'])
    # current_price = float(info[0]['regularMarketPrice'])
    # dividend_per_share = float(dividend_yield * current_price)
    # market_cap = float(info[0]['marketCap'])
    # shares = float(info[0]['sharesOutstanding'])
    # market_cap = float(info[0][''])
    # market_cap = float(info[0][''])
    # payout_ratio = float(info[0]['payoutRatio'])
    # value_ddm = dividend / discount_rate
    # calculated_price = market_cap / shares


    #rendering the webpage, importing variables
    return render_template("valuation.html", 
    ticker=ticker, 
    info=info, 
    # company_details=company_details,
    # current_price=current_price, 
    # dividend_yield=dividend_yield,
    # dividend_per_share=dividend_per_share,
    # market_cap=market_cap,
    # shares=shares,
    # calculated_price=calculated_price,
    revenues=revenues,
    bs=bs,
    cf=cf,
    major_holders=major_holders,
    institutional_holders=institutional_holders,
    # value_ddm=value_ddm, 
    # discount_rate=discount_rate)
    )

  else:
    return render_template("valuation.html")



app.run(host='127.0.0.1', port=8000)

