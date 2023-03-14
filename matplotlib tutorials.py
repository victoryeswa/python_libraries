import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Basic graph
x = [1,2,3]
y = [2,4,6]

#resize your graph
plt.figure(figsize=(5,3), dpi=100)
plt.plot(x,y, label='2x', color ='yellow',linewidth=2, marker='.',linestyle='--',markersize=10, markeredgecolor='blue')
# line number two
x2 =np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='x^2')
plt.plot(x2[5:],x2[5:]**2, 'r--')
plt.legend()

#plot labels
plt.xlabel('x-label')
plt.ylabel('y-label')
#title
plt.title('My first Graph', fontdict={'fontname':'', 'fontsize':20})
plt.style.use('Solarize_Light2')
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,7,10])

#to save your plot
plt.savefig('mygrapgh.png', dpi=100)
plt.show()

#using a short hand notation
# fmt = '[color][marker][line]
x = [2,4,5,7]
y = [3,6,9,12]
plt.plot(x,y, 'r.-', label='2x')
plt.show()
#bar charts