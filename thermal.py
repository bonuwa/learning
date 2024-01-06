import pandas as pd

df = pd.read_excel(".\input.xlsx")

print(df)

df2 = df.map(lambda e: e + 10)

mw = df.mean(axis='index')
print(mw)

df2.to_csv('.\output.csv')

df3 = pd.read_csv(".\output.csv")

pd.read
print(df3)