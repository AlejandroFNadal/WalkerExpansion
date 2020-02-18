import numpy as np
import matplotlib.pyplot as plt

x=np.array([])
y=np.array([])
rarr=np.array([])
def chaos(r, x_n):
    return r*x_n*(1-x_n)

R=3.7
x_n=0.2
time=1 
for time in range(1,100):
    x_n=chaos(R,x_n)
    x=np.append(x,[time])
    y=np.append(y,[x_n])
    print(x_n)
    
    #rarr=np.append(rarr,[R])
    #R=R+0.01

plt.plot(x,y)
plt.show()
