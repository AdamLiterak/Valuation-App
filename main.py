from flask import Flask, render_template, request
import yfinance as yf

#export FLASK_APP=main.py
#q for exiting git commands in terminal
#token: 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
#test1

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/valuation', methods=["GET", "POST"])
def valuation():
  ticker = request.form.get("ticker")
  if request.method == "POST":

    return render_template("valuation.html", ticker=ticker)

  else:
    return render_template("valuation.html", ticker=ticker)

app.run(host='0.0.0.0', port=8080)

