import math
import numpy as np
import matplotlib.pyplot as plt

msize = [5, 15, 50]

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**3.5 - 2**10, 'bs', t, 100*t**2.1 + 50, 'g^')
for item in msize:
    t = np.arange(0, item, 0.1)
    plt.plot(t, (2**10)*t + (2**10) , 'red', t, t**3.5 - 1000, 'blue', t, 100*t**2.1 + 50, 'green')
    plt.xlim(0, item)
    plt.rcParams["figure.figsize"] = (7,7)
    plt.show()
