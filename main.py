import numpy as np
import matplotlib.pyplot as plt

#constants
rm = 10
rf = 7

Sf = 200
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

#Derivative
def VF(u,v,w):
    return [da(u,v),dm(u,v,w),df(u,v,w)]

#Orbit Integration
def streamline(start_point, vector_field, dt = 0.1, steps = 3000):
    path = [start_point]
    current_point = np.array(start_point)
    for _ in range(steps):
        u, v, w = vector_field(*current_point)
        direction = np.array([u,v,w])
        current_point = current_point+direction*dt
        path.append(current_point)
    return np.array(path)

#Seed Points
M = M_limit(F_limit)

a = np.linspace(0,1,10)
m = np.linspace(0,np.max(M),10)
f = np.linspace(0,int(Sf/rf),10)
seed_points = np.stack((a,m,f),axis=-1)

#Plotting
ax = plt.figure().add_subplot(projection='3d')

ax.plot(F_limit,M_limit(F_limit),zs=0,zdir='z')

for point in seed_points:
    orbit = streamline(point,VF)
    ax.plot3D(orbit[:,0],orbit[:,1],orbit[:,2])

plt.show()



