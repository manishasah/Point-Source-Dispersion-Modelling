from pointSource import *
import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(0, x, 10)
ylist = np.linspace(-y, y, 10)
X, Y = np.meshgrid(xlist, ylist)

#calculates and plot concentration at different values of x and y at a given z
C = point_conc(X, Y, z)
plt.figure()
cp = plt.contourf(X, Y, C)
plt.colorbar(cp)
plt.clabel(cp, inline=1, fontsize=10)
plt.title('Horizontal Dispersion at given height')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()



zlist = np.linspace(0, z, 10)
X, Z = np.meshgrid(xlist, zlist)
#calculates and plot concentration at different values of x and z at a given y
C = point_conc(X, y, Z)
plt.figure()
cp = plt.contourf(X, Z, C)
plt.colorbar(cp)
plt.clabel(cp, inline=1, fontsize=10)
plt.title('Vertical Dispersion')
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.show()




