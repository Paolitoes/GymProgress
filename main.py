import numpy as np
import matplotlib.pyplot as plt

#constants
rm = 10
rf = 7

Sf = 3000
m_max = 220

def M_limit(F):
    M_temp =(Sf-rf*F)/rm
    M_temp[M_temp>m_max]=m_max
    return M_temp

F_limit = np.linspace(0,int(Sf/rf),20)

fig, ax = plt.subplots()
ax.plot(F_limit,M_limit(F_limit))
plt.show()



