import pandas as pd

df = pd.read_csv('/home/omnya/Documents/GitHub/advanced-python/weather.csv')
#basics

print(df.head(2))

print(df.columns)
print(df.shape)
print(df.tail(3))# last 3 rows