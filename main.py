from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

from helpers import add, stock_screener

#export FLASK_APP=main.py
#q for exiting git commands in terminal
#token: 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
#test1
#test2

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/valuation', methods=["GET", "POST"])
def valuation():

  if request.method == "POST":
    ticker = request.form.get("ticker")
    ticker_list = [ticker]
    fundamentals_list = ['shortName','sector','forwardEps','trailingPE','forwardPE','pegRatio','priceToBook','profitMargins','enterpriseToEbitda',
    'enterpriseToRevenue','country','industry','regularMarketPrice','marketCap','sharesOutstanding']

    info = stock_screener(ticker_list, fundamentals_list)



    return render_template("valuation.html", ticker=ticker, info=info)

  else:
    return render_template("valuation.html")

app.run(host='0.0.0.0', port=8080)

