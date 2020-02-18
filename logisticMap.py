import numpy as np
import matplotlib.pyplot as plt

x = np.array([])
y = np.array([])


def equation(r, x_n):
    return r*x_n*(1-x_n)


''' ALTERNATIVA 1'''
# R = 1
# x_n = 0.2
# time = 1

# for time in range(1, 100):
#     x_n = logisticMap(R, x_n)
#     x = np.append(x, [time])

#     print(x_n)
# y = np.append(y, [x_n])
# R = R+0.01

# plt.plot(x, y, 'bs')
# plt.show()

'''ALTERNATIVA 2'''


def logisticMap(x_0, r, i):
    xt = []
    T = []
    t = 0
    for i in range(1, 100):

        xt.append(x)
        T.append(t)
        t += 1
        x = equation(r, i)
    plt.plot(T, xt)
    plt.ylim(0, 100)
    plt.xlim(0, T[-1])
    plt.show
