import re
from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
from cs50 import SQL
from helpers import add, stock_screener
import pandas as pd

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
def growth(start,end):
  return (end/start-1)

def cagr(start,end,periods):
  '''calculates CAGR, periods calculated (end_year - start_year)'''
  return ((end/start)**(1/periods))-1

def numbers(number):
  return int(number/1000)

def to_number_1(x):
  '''function to format numbers'''
  if type(x) == str:
      return x
  elif (type(x) == int) or (type(x) == float):
      return "{:,}".format(x)
  else:
      return "error"


# CONTEXT PROCESSORS
@app.context_processor
def utility_processor():

  def to_number(x):
    '''function to format numbers'''
    if type(x) == str:
        return x
    elif (type(x) == int) or (type(x) == float):
        return "{:,}".format(x)
    else:
        return "error"

  return dict(to_number=to_number)


#ROUTES
@app.route('/')
def hello_world():
  return render_template("index.html")


@app.route('/model', methods=["GET","POST"])
def model():
  if request.method == "POST":
    ticker = request.form.get("ticker")

    #first version - to be deleted later
    pnl = db.execute(queries_list[0], ticker)
    columns = []
    for i in pnl[0]:
      columns.append(i)
    
    # PANDAS DF VERSION
    period_max = int(db.execute(queries_list[2], ticker)[0]['MAX(period)'])
    period_min = period_max - 7
    pnl_df = pd.DataFrame(db.execute(queries_list[1], ticker, period_min))
    pnl_df_pivoted = pnl_df.pivot(index="item",columns="period",values="value").rename_axis(None)

    # connecting to the mapping
    mapping = pd.read_csv("mapping.csv").set_index("item")
    pnl = pnl_df_pivoted.merge(mapping, left_index=True, right_index=True).sort_values('order').set_index('name').rename_axis(None)
    pnl = pnl.iloc[:,0:(len(list(pnl.columns))-1)]



    pnl_columns = list(pnl_df_pivoted.columns)
    
    pnl_dict = pnl_df_pivoted.to_dict()
    # pnl_columns_dict = pnl_columns.to_dict()

    # rendering the tenplate with all the values
    return render_template("model.html",

    tables=[pnl_df_pivoted.to_html(classes='df_table', float_format='{:,}'.format, header=True),
    pnl.to_html(classes='df_table', float_format='{:,.0f}'.format, header=True)],

    columns=columns, 
    pnl=pnl, 
    pnl_df_pivoted = pnl_df_pivoted, 
    pnl_columns = pnl_columns, 
    pnl_dict=pnl_dict, 
    pnl_df=pnl_df)

  else:
    return render_template("model.html")


@app.route('/assumptions', methods=["GET","POST"])
def assumptions():
  if request.method == "POST":
    ticker = request.form.get("ticker")
    years = int(request.form.get("years"))
    revenueGrowth = request.form.get("revenueGrowth")
    ebitdaMargin = request.form.get("ebitdaMargin")
    wacc = request.form.get("wacc")

    for i in range(years):
      db.execute(queries_list[3], ticker, i+1, "revenueGrowth", revenueGrowth)
      db.execute(queries_list[3], ticker, i+1, "ebitdaMargin", ebitdaMargin)
      db.execute(queries_list[3], ticker, i+1, "wacc", wacc)

    return render_template("assumptions.html")
  else:
    return render_template("assumptions.html")


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

