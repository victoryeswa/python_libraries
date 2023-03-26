import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
# pd.set_option('max_columns', 200)

#import data 

df  = pd.read_csv('January_data.csv')
print(df.head(2))
# data understanding
print(df.shape)
print(df.columns)

#subset columns (later)


#first find d.type
print(df.dtypes)

#information about numeric data in our dataset
print(df.describe())

#2. DAta preparation
# - dropping irrelevant columns and rows
#identifying duplicated columns, renaming columns,feature creation

print(df.columns)

df2 = df[[#'unnamed: 0', 
         'Order ID', 'Product', 'Quantity Ordered', 'Price Each',
       'Order Date', 'Purchase Address']]

print(df2)
#alternatively the drop method can be used

df3 = df.copy()

#example of dropping columns
df3 = df3.drop(['Product'], axis=1)

print(df.columns)
print(df2.columns)
print(df3.columns)

print(df3.head(2))

#rename our columns 
df = df.rename(columns= {'Order ID': 'Order_ID'})

print(df.columns)

#to check the null values
print(df.isna())

#returns the sum of all null values
print(df.isna().sum())

#checking duplicate data
#ignores the first row thats a duplicate
df.duplicated()

#locate in the dataset

df5 = df.loc[df.duplicated()]

print(df5)

df6 = df.loc[df.duplicated(subset=['Product'])]

print(df6, 'subset')

#query#checking an example duplicate
df7 = df.query('Product == "Phone"')
print(df7) #gives the list of the duplicates

print(df.columns)

#to check the below did not work
df7 = df.loc[~df.duplicated(subset=['Product', 'Order_ID'])] \
        .reset_index(drop=True)
print(df7, 'two columns')


