import matplotlib.pyplot as plt
import numpy as np
# values of x and y axes
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]
plt.plot(x, y, 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
# 0 is the initial value, 51 is the final value
# (last value is not taken) and 5 is the difference
# of values between two consecutive ticks
plt.xticks(np.arange(0, 51, 5))
plt.yticks(np.arange(0, 11, 1))
plt.tick_params(axis='y',colors='red',rotation=45)
plt.show()