import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
#pd.set_option('max_columns', 200)

#import data

df = pd.read_csv('January_data.csv')

print(df.tail(2))

#feature understanding
#plotting featuree Distributions
# histogram, KDE, Boxplot
print(df['Product'])

df1 = df['Product'].value_counts()\
        .head(5) \
        .plot(kind='bar', title='Top Products')

df1.set_xlabel('year introduced')
df1.set_ylabel('Quantity')
plt.show()
print(df1, 'value counts')

df3 = df['Quantity Ordered'].plot(kind='hist', bins=20, title ='Quantity Ordered')

print(df3)
print(df.columns)
plt.show()