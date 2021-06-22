import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(10)]
print(x)
y = [2*i for i in range(10)]
print(y)
plt.xlabel('x axis')
plt.ylabel('y axis')
#plt.plot(x, y)
plt.scatter(x, y)
plt.show()
