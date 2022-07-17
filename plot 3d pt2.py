import numpy as np
import matplotlib.pyplot as plt

N = 50
nilai_x = np.linspace(-5, 5, N)
nilai_y = np.linspace(-5, 5, N)


def function_z (x, y): 
    z = 50 - (x**2 + y**2)
    return z

x, y = np.meshgrid(nilai_x, nilai_y)
z = function_z(x, y)
print(z)


ax = plt.axes(projection = '3d')
ax.plot_surface(x, y, z)
# ax.plot_wireframe(x, y, z)
plt.show()