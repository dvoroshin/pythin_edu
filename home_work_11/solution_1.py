import matplotlib.pyplot as plt

x_list = []
y_list = []

for x in range(-10,11):
    y = 5*x*x+10*x-30
    x_list.append(x)
    y_list.append(y)

plt.axhline(y = 0, color = 'r', linestyle = '--')
plt.plot(y_list)
plt.show()
