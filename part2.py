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
x=[]
y=[]
for i in range(0,len(Epsilon_list)):
    temp=np.zeros(10000)
    temp2=np.zeros(10000)
    x.append(temp)
    y.append(temp2)

Population_list=[]
for i in range(0, len(Epsilon_list)):
    temp2=np.ones(1000)
    Population_list.append(temp2)


pop_counter=0 #current population
ep_cont=0# counts elements for the arrays that will contain M_n vs M_n+1
for epsilon in Epsilon_list:
    m=M(Population_list[pop_counter])
    for j in range(1,10000):
        x[ep_cont][j]=m
        Population_list[pop_counter]=model(epsilon,rvalues,Population_list[pop_counter])
        m=M(Population_list[pop_counter])
        y[ep_cont][j]=m
    ep_cont+=1
    pop_counter+=1


plt.plot(x[0],y[1],'rs',x[1],y[1],'bs',x[2],y[2],'gs',x[3],y[3],'cs',x[4],y[4],'ms',x[5],y[5],'ys',x[6],y[6],'rs',x[7],y[7],'k+',markersize=0.5)
plt.show()

#Part Three here