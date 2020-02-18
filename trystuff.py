#Number of populations =1000, equivalent to Walker
N=1000
#maximum size for all populations = 100
K=100
populations=[] 

def f_i(r,x_i):
    return r*x_i*(1-x_i/K)

for i in range(0,N):
    populations.append(1) #creating 1000 populations of x_i,0=1

def m_n(r):
    sum=0
    for elem in populations:
        sum=sum+f_i(r,elem)
    sum=sum/N
    return sum

def M(r):
    sum=0
    for elem in populations:
        sum=sum+elem
    sum=sum/N
    return sum
