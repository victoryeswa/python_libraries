import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
#pd.set_option('max_columns', 200)
#pd.set_option('max_columns', 200)

df = pd.read_csv('January_data.csv')

print(df.head(3))
print(df.columns)

df1 = df.plot(kind='scatter', x='Product', y='Quantity Ordered', title='Sales distribution')

print(df1)
plt.show()

df = sns.scatterplot(x='Product', y='Quantity Ordered', hue='Product')
df.set_title('Sales per product')

plt.show()