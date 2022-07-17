import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 5)
y = [11, 22, 33, 44 ,55]
z = [4, 6, 10, 8, 9]

ax = plt.axes(projection = '3d')
ax.scatter3D(x, y, z, s = 100)

ax.set_xlabel('sumbu x')
ax.set_ylabel('sumbu y')
ax.set_zlabel('sumbu z')

plt.show()
