import matplotlib.pyplot as plt
import numpy as np
from random import uniform
#Number of populations =1000, equivalent to Walker
N=1000
#maximum size for all populations = 100
K=100

populations=np.ones(1000)

#create R values
rvallist=[]
for i in range(0,1000):
    rvallist.append(uniform(3.9,4.0))
rvalues=np.array(rvallist)

#All these functions are explained in the Walker paper
def f_i(r,pop):
    return r*pop*(1-pop/K)
    

def m_n(r,pop):
    return f_i(r,pop).sum()/N

def M(pop):
    return pop.sum()/N

def model(epsilon,r,populations):
    populations=(1-epsilon)*f_i(r,populations)+epsilon*m_n(r,populations)
    return populations

#list of values of epsilon

Epsilon_list=[0,0.075,0.1,0.2,0.225,0.25,0.3,0.4]

#list of numpy arrays of M and M+1
M_values=[]
for i in range(0,len(Epsilon_list)):
    temp=np.zeros(1000)
    M_values.append(temp)
    M_values.append(temp)
#list of populations
'''
Population_list=[]
for i in range(0, len(Epsilon_list)):
    temp2=np.ones(1000)
    Population_list.append(temp2)
pop_counter=0 #current population
ep_cont=0# counts elements for the arrays that will contain M_n vs M_n+1
for epsilon in Epsilon_list:
    m=M(Population_list[pop_counter])
    for j in range(1,1000):
        M_values[ep_cont][j]=m
        Population_list[pop_counter]=model(epsilon,rvalues,Population_list[pop_counter])
        m=M(Population_list[pop_counter])
        ep_cont+=1
        M_values[ep_cont][j]=m
        ep_cont-=1
    ep_cont+=2
    pop_counter+=1


plt.plot(M_values[0],M_values[1],'rs',M_values[2],M_values[3],'bs',M_values[4],M_values[5],'ks',markersize=1)
plt.show()
'''
x=np.zeros(1000)
y=np.zeros(1000)
m=M(populations)
for j in range(1,1000):
    #print(j)
    x[j]=m
    #x=np.append(x,[m])
    populations=model(0.075,rvalues,populations)
    m=M(populations)
    #y=np.append(y,[m])
    y[j]=m
populations=np.ones(1000)
x2=np.zeros(1000)
y2=np.zeros(1000)
m=M(populations)
for j in range(1,1000):
    #print(j)
    x2[j]=m
    #x=np.append(x,[m])
    populations=model(0.1,rvalues,populations)
    m=M(populations)
    #y=np.append(y,[m])
    y2[j]=m
populations=np.ones(1000)
x3=np.zeros(1000)
y3=np.zeros(1000)
m=M(populations)
for j in range(1,1000):
    #print(j)
    x3[j]=m
    #x=np.append(x,[m])
    populations=model(0.3,rvalues,populations)
    m=M(populations)
    #y=np.append(y,[m])
    y3[j]=m
plt.plot(x,y,'rs',x2,y2,'bs',x3,y3,'ks',markersize=1)
plt.show()
#print(populations)
'''

x2=np.zeros(100)
y2=np.zeros(100)
populations=np.ones(100)
for j in range(1,100):
    print(j)
    x2[j]=m
    model(0.1,3.9,populations)
    m=M(populations)
    y2[j]=m

x3=np.zeros(100)
y3=np.zeros(100)
populations=np.ones(100)
for j in range(1,100):
    print(j)
    x3[j]=m
    model(0.3,3.9,populations)
    m=M(populations)
    y3[j]=m

'''