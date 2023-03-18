import pandas as pd
import numpy as np
import datetime
import random

products = {
    #product:price
    'iphone':[700, 10],
    'Google Phone':[600, 8],
    'Verybad Phone': [400, 3],
    '20in Monitor':[109.99, 6],
    '34in Ultrawide Monitor': [379.99, 9],
    '27in 4k Gaming Monitor': [389.99, 9],
    '27in FHD Monitor': [149.99, 11],
    'Flatscreen Tv': [300, 7],
    'Macbook Pro Laptop': [1700, 7],
    'Thinkpad Laptop': [999.99, 6],
    'AA Batteries (4-pack)': [3.84, 30],
    'AAA Batteries (4-pack)': [2.99, 30],
    'USB-C Charging Cable': [11.95, 30],
    'Lightning Charging Cable': [14.95,30],
    'wired Headphones': [11.99, 26],
    'Bose Soundsport Headphones': [99.99, 19],
    'Apple Airpods Headphones': [150,22], 
    'LG Washing Machine': [600.00, 1],
    'LG Dryer':[600.00, 1]
}
columns = ['Order ID', 'Product', 'Quantity Ordered','Price Each', 'Order Date', 'Purchase Address' ]


df = pd.DataFrame(columns = columns)

for i in range(1000):
    product_list = [product for product in products]
    weights = [products[product][1]for product in products]

    product = random.choices(product_list, weights=weights)[0]
    price = products[product]
    df.loc[i] =  [i, product, 1, price, 'NA', 'NA']

print(product_list)
print(weights)

df.to_csv('test_data.csv')