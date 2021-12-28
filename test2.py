import pandas as pd
from cs50 import SQL
db = SQL("sqlite:///data_1.db")

dictionary = db.execute("SELECT * FROM financials WHERE (item='revenue' OR item='grossProfit') AND (period > 2018);")

dataframe = pd.DataFrame(dictionary)

dataframe_pivoted = dataframe.pivot(index="item",columns="period",values="value").rename_axis(None)
print(dataframe_pivoted)

# year_max = int(db.execute("SELECT MAX(period) FROM financials WHERE (ticker like ?) AND (type like ?);", "AAPL", "PNL")[0]['MAX(period)'])
# print(year_max)
# year_min = year_max - 4
# print(year_min)

print(dataframe_pivoted[2019])

d = {"revenue":[1,"Revenue"], "grossProfit":[2,"Gross Profit"]}
dataframe_1 = pd.DataFrame(d)

print(dataframe_1)
dataframe_2 = dataframe_1.T.set_axis(["order","name"], axis=1)
print(dataframe_2)

new_df = dataframe_pivoted.merge(dataframe_2, left_index=True, right_index=True).sort_values(by=['order'])

print(new_df)

new_df_1 = new_df.set_index('name').rename_axis(None).iloc[:,0:3]
print(new_df_1)

print(len(list(new_df_1.columns)))


df_4 = pd.read_csv("mapping.csv")
# .set_index("item")
print(df_4)

df_5 = dataframe_pivoted.merge(df_4, left_index=True, right_on='item').sort_values('order').set_index('name')
print(df_5)