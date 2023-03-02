import matplotlib.pyplot as plt
import numpy as np

size = 15
houses = np.random.randint(100, 300, size)
prices = np.rnadom.randint(3000000, 20000000, size)
mean_pr = [round(prices[i]/houses[i]) for i in range(len(prices))]
h_names = ['house 1',
           'house 2',
           'house 3',
           'house 4',
           'house 5',
           'house 6',
           'house 7',
           'house 8',
           'house 9',
           'house 10',
           'house 11',
           'house 12',
           'house 13',
           'house 14',
           'house 15']

plt.axhline(y = 50000, color = 'g', linestyle = 'dotes')
plt.bar(h_names,mean_pr,linewidth=0.5)
plt.show()