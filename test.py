import numpy as np
import matplotlib.pyplot as plt

dx = 0.2
nx = int(10 / dx)
dt = 0.01
nt = int(10/dt) # dibuat variasi dengan t = 10,100, dan lain-lain
T = np.zeros(nx + 1)
#T2 = np.zeros(nx + 1)
dT = np.zeros(nx + 1)

T[0] = 100
#T2[0] = 100

for n in range(1, nt+1, 1):
    for i in range(1, nx, 1):
        dT[i] = (T[i-1] - 2*T[i] + T[i+1])
    dT[nx] = 2 * T[nx-1] - 2*T[nx] # 
    print(dT[nx])
    dT = (dT * dt)/dx**2
    T = T + dT

plt.plot(T)
plt.ylim(0,100)
plt.ylabel("suhu")
plt.grid(True)
plt.show()