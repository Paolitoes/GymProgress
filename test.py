import numpy as np

x = np.linspace(0,10,10)
y = np.linspace(0,12,12)

X,Y = np.meshgrid(x,y)

print(x)
print("Following this is big X")
print(X.shape)
