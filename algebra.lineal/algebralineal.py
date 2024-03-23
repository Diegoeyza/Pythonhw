import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
v1, v2, v3 = np.array([1,2,3]), np.array([1,-1,0]), np.array([1,1,0])
#P1
p1 = v1
d1 = v2-v1
t = np.arange(-5,5,0.1) 
X = p1[0]+t*d1[0] 
Y = p1[1]+t*d1[1]
Z = p1[2]+t*d1[2]
fig = plt.figure() 
ax = Axes3D(fig)
ax.plot3D(X,Y,Z) 
#P2
p2 = v1
d2 = v3-v1
t=np.arange(-5,5,0.1) 
X = p2[0]+t*d2[0] 
Y = p2[1]+t*d2[1]
Z = p2[2]+t*d2[2]
fig = plt.figure() 
ax = Axes3D(fig)
ax.plot3D(X,Y,Z) 
#P3 
#ec cartesiana 3x + 3y - 3z = 0
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y) 
Z = X + Y
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='bone')
plt.show() 
#P4
#ec cartesiana -x - y + z*0 + 2 = 0
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y) 
Z = X + Y - 2
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='bone')
plt.show()


