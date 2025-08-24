import numpy as np
import matplotlib.pyplot as plt

#constants
rm = 10
rf = 7

Sf = 3000
m_max = 220

cm = 1700
cf = 1200

ka = 1

#System of Equations
def S(M,F):
    return m_max - rm*M-rf*F

def dm(A,M,F):
    t1 = A*S(M,F)/cm
    t2 = (1-M/m_max)
    return t1*t2

def df(A,M,F):
    return (1-A)*S(M,F)/cf

def da(A,M):
    t1 = ka*(1-A)
    t2 = (1-M/m_max)
    return t1*t2

#Boundary Calculations
def M_limit(F):
    M_temp =(Sf-rf*F)/rm
    M_temp[M_temp>m_max]=m_max
    return M_temp

F_limit = np.linspace(0,int(Sf/rf),20)

#Cords 
a = np.linspace(0,1,20)
m = np.linspace(0,m_max,30)
f = np.linspace(0,int(Sf/rf),20)

A,M,F = np.meshgrid(a,m,f)



#Plotting
ax = plt.figure().add_subplot(projection='3d')
ax.plot(F_limit,M_limit(F_limit),zs=0,zdir='z')
plt.show()



