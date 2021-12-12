from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

from cs50 import SQL

from helpers import add, stock_screener

#export FLASK_APP=main.py
#q for exiting git commands in terminal
#token: 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
#test1
#test2

app = Flask(__name__)

db = SQL("sqlite:///data.db")

@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/valuation', methods=["GET", "POST"])
def valuation():

  if request.method == "POST":
    ticker = request.form.get("ticker")
    ticker_list = [ticker]
    discount_rate = request.form.get("discount_rate")

    info = stock_screener(ticker_list)

    company_details = info[0]['longBusinessSummary']

    #dividend discount model
    dividend_yield = float(info[0]['dividendYield'])
    current_price = float(info[0]['currentPrice'])
    dividend = float(dividend_yield * current_price)
    payout_ratio = float(info[0]['payoutRatio'])
    value_ddm = dividend / discount_rate



    return render_template("valuation.html", ticker=ticker, info=info, company_details=company_details, dividend=dividend, payout_ratio=payout_ratio, value_ddm=value_ddm, discount_rate=discount_rate)

  else:
    return render_template("valuation.html")



app.run(host='127.0.0.1', port=8000)

