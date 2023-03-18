import numpy as np
import pandas as pd
import datetime
import random
import calendar



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

def generate_random_time():
      #generate a date in the format mm/dd/yy-h:m
      day_range = calendar.monthrange(2019, month)[1]
      random_day = random.randint(1, day_range)
      if random.random() < 0.5:
            date = datetime.datetime(2019, month, ranom_day, 12, 0)
      else:
            date = datetime.datetime(2019, month, random_day, 20,0 )
      time_offset = np.random.normal(loc=0, scale=180)

      final_date = date + datetime.timedelta(minutes=time_offset)

      return final_date.strftime('%m/%d/%y %H:%M')


def generate_random_address():
      street_names = ['Main', '2nd', '1st', '4th', '5th', '6th', '7th', 'maple', 'Pine', 'Washington', '8th', 'Cedar', 'Eln', 'Walnut']
      
      cities = ['San francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland', 'Los Angeles', 'Seattle' ]
      weights = [9,4,5,2,3,3,2,0.5,6,3]
      states = ['CA', 'MA', 'NY', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']
      zips =  ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']

      street = random.choice(street_names)
      index = random.choices(range(len(cities)), weights=weights)[0]

      return f'{random.randint(1, 999)} {street} st, {cities[index]}, {states[index]} {zips[index]}'

def write_row(order_id,product, order_date, address):
      price = products[product][0]
      quantity_ordered = np.random.geometric(p=1.0-(1.0/price), size=1)[0]
      return [order_id, product, quantity_ordered, price, date, address]

product_list = [product for product in products]
weights = [products[product][1] for product in products]
columns = ['Order ID', 'Product', 'Quantity Ordered','Price Each', 'Order Date', 'Purchase Address' ]

order_id = 143253
for month_value in range(1, 13):        


        if month_value <=10:
            #orders_amount = int(np.random.normal(loc=12000, scale=4000))
            orders_amount = 100

        if month_value ==11:
              orders_amount = int(np.random.normal(loc=20000, scale=3000))

            #make slightly higher
        if month_value ==12:
              orders_amount = int(np.random.normal(loc=26000, scale=3000))

              
        #make value higher 

        df = pd.DataFrame(columns=columns)

        #for i in range(orders_amount):
        i=0
        while orders_amount >0:

            address = generate_random_address()
            date = generate_random_time(month_value)   
            

            product = random.choices(product_list, weights=weights)[0]
            #price = products[product][0]
            #quantity_ordered = np.random.geometric(p-1.0-(1.0/price), size=1)[0]
            df.loc[i] = write_row(order_id, product, date, address)

            if product == 'iphone':
                  if random.random() < 0.05:
                        df.loc[i] = write_row(order_id, 'Lightning Charging Cable', date, address)
                        i+=1

                        #df.loc[i] = [order_id, 'lightning Charging Cable', quantity_ordered, price, date, address]

            order_id +=1
            orders_amount -=1

        month_name = calendar.month_name[month_value]

        print(month_name + 'finished!!')
        df.to_csv(f'{month_name}_data.csv')
        break