import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Basic graph
x = [1,2,3]
y = [2,4,6]
plt.plot(x,y, label='2x', color ='yellow',linewidth=2, marker='_',markersize=10)
plt.legend()
#title
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('My first Graph', fontdict={'fontname':'', 'fontsize':20})
plt.style.use('Solarize_Light2')
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,7,10])
plt.show()
