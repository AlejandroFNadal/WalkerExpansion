import numpy as np
import matplotlib.pyplot as plt

x = np.array([])
y = np.array([])


def logisticMap(r, x_n):
    return r*x_n*(1-x_n)


R = 1
x_n = 0.2
time = 1

for time in range(1, 100):
    x_n = logisticMap(R, x_n)
    x = np.append(x, [time])

    print(x_n)
y = np.append(y, [x_n])
R = R+0.01

plt.plot(x, y, 'bs')
plt.show()
