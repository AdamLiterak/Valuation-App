import json
from cs50 import SQL

db = SQL("sqlite:///data_1.db")
text = open("aapl.txt","r").read()
text_json = json.loads(text)
# text.close()

def save_data_from_fmp():
    db.execute("")

type_pnl = "PNL"
type_bs = "BS"

items_pnl = ['revenue', 'costOfRevenue', 'grossProfit', 'researchAndDevelopmentExpenses',
            'generalAndAdministrativeExpenses', 'sellingAndMarketingExpenses', 'sellingGeneralAndAdministrativeExpenses',
            'otherExpenses', 'operatingExpenses', 'costAndExpenses', 'interestIncome', 'interestExpense',
            'depreciationAndAmortization', 'ebitda', 'operatingIncome',
            'totalOtherIncomeExpensesNet', 'incomeBeforeTax', 'incomeTaxExpense', 'netIncome']

items_bs = [ 
            'cashAndCashEquivalents', 'shortTermInvestments', 'cashAndShortTermInvestments', 'netReceivables', 'inventory', 
            'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet', 'goodwill', 'intangibleAssets', 
            'goodwillAndIntangibleAssets', 'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets', 'totalNonCurrentAssets', 
            'otherAssets', 'totalAssets', 'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue', 'otherCurrentLiabilities', 
            'totalCurrentLiabilities', 'longTermDebt', 'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent', 
            'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities', 'otherLiabilities', 'capitalLeaseObligations', 
            'totalLiabilities', 'preferredStock', 'commonStock', 'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss', 
            'othertotalStockholdersEquity', 'totalStockholdersEquity', 'totalLiabilitiesAndStockholdersEquity', 'minorityInterest', 
            'totalEquity', 'totalLiabilitiesAndTotalEquity', 'totalInvestments', 'totalDebt', 'netDebt']

# for i in text_json:
#     date = i["date"]
#     currency = i["reportedCurrency"]
#     ticker = i["symbol"]
#     revenue = i["revenue"]

for i in text_json:
    ticker = i["symbol"]
    period = i["date"][0:4] #year instead?
    currency = i["reportedCurrency"]
    type = type_pnl
    items = items_pnl
    for j in items:
        item = j
        value = i[j]
        db.execute("INSERT INTO financials (ticker, period, item, value, currency, type) VALUEs (?,?,?,?,?,?);",ticker,period,item,value,currency,type)


# ['date', 'symbol', 'reportedCurrency', 'cik', 'fillingDate', 'acceptedDate', 'calendarYear', 'period',
#  'revenue', 'costOfRevenue', 'grossProfit', 'grossProfitRatio', 'researchAndDevelopmentExpenses',
#  'generalAndAdministrativeExpenses', 'sellingAndMarketingExpenses', 'sellingGeneralAndAdministrativeExpenses',
#  'otherExpenses', 'operatingExpenses', 'costAndExpenses', 'interestIncome', 'interestExpense',
#  'depreciationAndAmortization', 'ebitda', 'ebitdaratio', 'operatingIncome', 'operatingIncomeRatio',
#  'totalOtherIncomeExpensesNet', 'incomeBeforeTax', 'incomeBeforeTaxRatio', 'incomeTaxExpense', 'netIncome',
#  'netIncomeRatio', 'eps', 'epsdiluted', 'weightedAverageShsOut', 'weightedAverageShsOutDil', 'link', 'finalLink']

# ['date', 'symbol', 'reportedCurrency', 'cik', 'fillingDate', 'acceptedDate', 'calendarYear', 'period', 
# 'cashAndCashEquivalents', 'shortTermInvestments', 'cashAndShortTermInvestments', 'netReceivables', 'inventory', 
# 'otherCurrentAssets', 'totalCurrentAssets', 'propertyPlantEquipmentNet', 'goodwill', 'intangibleAssets', 
# 'goodwillAndIntangibleAssets', 'longTermInvestments', 'taxAssets', 'otherNonCurrentAssets', 'totalNonCurrentAssets', 
# 'otherAssets', 'totalAssets', 'accountPayables', 'shortTermDebt', 'taxPayables', 'deferredRevenue', 'otherCurrentLiabilities', 
# 'totalCurrentLiabilities', 'longTermDebt', 'deferredRevenueNonCurrent', 'deferredTaxLiabilitiesNonCurrent', 
# 'otherNonCurrentLiabilities', 'totalNonCurrentLiabilities', 'otherLiabilities', 'capitalLeaseObligations', 
# 'totalLiabilities', 'preferredStock', 'commonStock', 'retainedEarnings', 'accumulatedOtherComprehensiveIncomeLoss', 
# 'othertotalStockholdersEquity', 'totalStockholdersEquity', 'totalLiabilitiesAndStockholdersEquity', 'minorityInterest', 
# 'totalEquity', 'totalLiabilitiesAndTotalEquity', 'totalInvestments', 'totalDebt', 'netDebt', 'link', 'finalLink']


#   "date" : "1986-09-30",
#   "symbol" : "AAPL",
#   "reportedCurrency" : "USD",
#   "cik" : "0000320193",
#   "fillingDate" : "1986-09-30",
#   "acceptedDate" : "1986-09-30",
#   "calendarYear" : "1986",
#   "period" : "FY",
#   "revenue" : 1901900000,
#   "costOfRevenue" : 840000000,
#   "grossProfit" : 1061900000,
#   "grossProfitRatio" : 0.5583364004416635,
#   "researchAndDevelopmentExpenses" : 0.0,
#   "generalAndAdministrativeExpenses" : 0.0,
#   "sellingAndMarketingExpenses" : 0.0,
#   "sellingGeneralAndAdministrativeExpenses" : 737300000,
#   "otherExpenses" : 51100000,
#   "operatingExpenses" : 788400000,
#   "costAndExpenses" : 1628400000,
#   "interestIncome" : 0.0,
#   "interestExpense" : 0.0,
#   "depreciationAndAmortization" : 51100000,
#   "ebitda" : 360900000,
#   "ebitdaratio" : 0.1897576108102424,
#   "operatingIncome" : 273500000,
#   "operatingIncomeRatio" : 0.16288974183711025,
#   "totalOtherIncomeExpensesNet" : -36300000,
#   "incomeBeforeTax" : 309800000,
#   "incomeBeforeTaxRatio" : 0.16288974183711025,
#   "incomeTaxExpense" : 155800000,
#   "netIncome" : 154000000,
#   "netIncomeRatio" : 0.08097165991902834,
#   "eps" : 0.010714,
#   "epsdiluted" : 0.010714,
#   "weightedAverageShsOut" : 14373333333,
#   "weightedAverageShsOutDil" : 14373333333,
#   "link" : "",
#   "finalLink" :