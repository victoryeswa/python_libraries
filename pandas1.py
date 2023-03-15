#loading data into pandas
#why pandas - flexibility, working with big data

import pandas as pd

df = pd.read_csv('/home/omnya/pokemon.csv')

print(df.head(3))
#Reading data in Pandas
##Read Headers
print(df.columns)
##read each column
print(df['Name'])
print(df[['Name','Type 1', 'HP']])

#Read each row
print(df.head(4))
print(df.iloc[1:4])
#read a specific location (R,C)
print(df.iloc[2,1])

#Using iter rows
for index, row in df.iterrows():
    print(index, row)
print(df.count())
#finding specific data in our dataset(textual based)
print(df.loc[df['Type 1']=='Grass'])
#sorting/describing data
print(df.describe())
#sorting
df.sort_values('Name', ascending=False)
print(df.sort_values(['Type 1','HP'],ascending=[0,1]).head(3))
#Making changes to data
df.head(2) #to check your dataframe
df['Totals'] = df['HP'] + df['Attack']+ df['Defense']+ df['Sp. Atk']+ df['Sp. Def'] + df['Speed']
print(df['Totals'])
#to drop a column
df = df.drop(columns=['Total'])
print(df.columns)
#making changes/ading a column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#to get columns as a list
cols = list(df.columns.values)
df = df[cols[0:4]+ [cols[-1]]+ cols[4:12]]
print(df.head(4))
#saving our new csv
df.to_csv('modified.1.csv', index=False)
df.to_excel('modified.xlsx', index=False)
#filtering Data
df.loc[df['Type 1']=='grass']
new_df = df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')]
new_df.to_csv('filtered.csv')
#setting an index
new_df.reset_index(drop=True, inplace=True)
print(new_df)
print(df)
#locate specific information - Names containing mega
df.loc[df['Name'].str.contains('Mega')]
#to get the reverse of mega
df.loc[~df['Name'].str.contains('Mega')]
#using regex expression
import re
#useful for complicated filtering.(based on certain textual patterns)
#flags = re.I - ignore case
df.loc[df['Type 1'].str.contains('Fire|Grass',flags = re.I,regex=True)]
df.loc[df['Name'].str.contains('pi[a-z]*',flags=re.I, regex=True )]
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] #only those that begin with pi
#Conditional Changes
df.loc[df['Type 1']=='Fire', 'Legendary']="True"

#changing multiple parameters at a time
df.loc[df['Total']>500, ['Generation', 'Legendary']] = 'TEST VALUE'
print(df)
# Aggregate Statistics(Group by)
df_new = df['Type 1'].mean().sort_values('Defense', ascending=False)
print(df_new)
df.groupby(['Type 1']).sum()
df['count'] = 1
df.groupby(['Type 1']).count()['count']
df.groupby(['Type 1', 'Type 2']).count()['count']
#working with large amounts of data
#for df in pd.read_csv('modified.csv', chunksize=100000):
 #   print('Chnk df')
  #  print(df)
new_df = pd.dataFrame(columns = df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1'].count())

    new_df = pd.concat([new_df, results])
    print(new_df)