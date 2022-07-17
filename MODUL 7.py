#MODUL 7 PRAKTIKUM KOMPUTASI GEOFISIKA
#LATIHAN 1

import numpy as np 
import matplotlib.pyplot as plt 

#PDE: Wave Equation
dx = 0.01
dt = 0.01
Nx = int(1/dx)
Nt = int(1/dt)
Nt = 80
u = np.zeros(Nx+1)
u1 = np.zeros(Nx+1)
u0 = np.zeros(Nx+1)
du = np.zeros(Nx+1)

x = np.linspace(0, 1, Nx+1)
x2 = (x-0.5)**2/(2*pow(10,-3))
v = 1


#initial condition
u = np.exp(-x2)

#Boundary Condition 
u[0] = 0
u[Nx] = 0
u1[0] = 0
u1[Nx] = 0

#time extrapolation
u0 = u

for i in range(1, Nt, 1):
    for j in range(1, Nx, 1):
        du[j] = ((u[j-1]-2*u[j]+u[j+1])/pow(dx,2))
    u1 = ((v*dt**2)*du)+(2*u)-u0
    u1[0] = 0
    u1[Nx] = 0
    u0, u = u, u1
    
plt.plot(x,u)
plt.ylim(-1,1)
plt.xlim(0,1)
plt.show()
