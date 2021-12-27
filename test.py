from cs50 import SQL

list_1 = ["revenue",
"costOfRevenue",
"grossProfit",
"researchAndDevelopmentExpenses",
"generalAndAdministrativeExpenses",
"sellingAndMarketingExpenses",
"sellingGeneralAndAdministrativeExpenses",
"otherExpenses",
"operatingExpenses",
"costAndExpenses",
"interestIncome",
"interestExpense",
"depreciationAndAmortization",
"ebitda",
"operatingIncome",
"totalOtherIncomeExpensesNet",
"incomeBeforeTax",
"incomeTaxExpense",
"netIncome"]

dict_1 = {}
z = 1
for i in list_1:
    dict_1[i] = z
    z += 1

print(dict_1)

db = SQL("sqlite:///data_1.db")

for i in dict_1:
    db.execute("INSERT INTO ordered (item, ordered, type) VALUES (?,?,?)", i, dict_1[i], "PNL")