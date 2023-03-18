people = {
    'first':['corey', 'jane', 'John'],
    'last':['schafer', 'Doe', 'Doe'],
    'email':['coreyschafer@gmail.com', 'Janejk@gmail.com', 'johndoe@gmail.com']


}

import pandas as pd

df = pd.DataFrame(people)

print(df.head())
#gives all the row that meet a filter criteria
print(df['last'] == 'Doe')

#example
filt = (df['last']=="Doe")

#apply the filter to a df

df[filt]# directly

#using the .loc index
#used to loook up rows/columns by label
df.loc[filt]

df2 = df.loc[filt, 'email']

print(df2)

#and or
filt = (df['first']=='Doe') & (df['last'] =='John')

print(filt)

df3 = df.loc[-filt, 'email']

print(df3, 'unfiltered')




