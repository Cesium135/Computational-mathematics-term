
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 8)
y= np.linspace(-2, 2, 8)
xgrid, ygrid = np.meshgrid(x, y)
z=2*(xgrid**3)-3*(ygrid**2)
plt.title("График функции z=2*x^3 - 3*y^2")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xgrid,ygrid,z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')