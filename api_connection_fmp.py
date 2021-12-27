#https://site.financialmodelingprep.com/developer/docs
#API KEY = ed10beffd26075cd6e5178bae356ca27
#my email / signed up with google
#free version up to 250 requests a day

import requests

api_key = "ed10beffd26075cd6e5178bae356ca27"
ticker = "AAPL"
# r = requests.get("https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=ed10beffd26075cd6e5178bae356ca27")
r = requests.get("https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?apikey=ed10beffd26075cd6e5178bae356ca27&limit=120")
print(r.text)

text_file = open("aapl_bs.txt","a")
text_file.write(r.text)