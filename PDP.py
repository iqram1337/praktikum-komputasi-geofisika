""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
import matplotlib.pyplot as plt
import numpy as np

dx = 0.01
dt = 0.01
nx = int(1/dx)
nt = int(1/dt)

uu = np.zeros(nx+1) 
u0 = np.zeros(nx+1)
u1 = np.zeros(nx+1)
du = np.zeros(nx+1)

nilai_x = np.linspace(0,1,nx+1)
x2 =  (nilai_x - 0.5)**2 / (2*pow(10,-3))
uu = np.exp(-x2)


uu[0] = 0
uu[nx] = 0


u0 = uu
u_akhir = np.zeros((nt+1, nx+1))
u_akhir[0,:] = uu 

for it in range(1,nt,1):
    for ix in range(1,nx,1):
        du[ix] = ((uu[ix-1] - 2*uu[ix] + uu[ix+1])/pow(dx,2))
    u1 = ((dt**2) * du) + (2*uu) - u0
    u1[0] = 0
    u1[nx] = 0
    u0, uu = uu, u1
    u_akhir[it, :] = u1

plt.plot(nilai_x, u_akhir[0,:], label='t=0')
plt.plot(nilai_x, u_akhir[20,:], label='t=0.2s')
plt.plot(nilai_x, u_akhir[40,:], label='t=0.4s')
plt.plot(nilai_x, u_akhir[50,:], label='t=0.5s')
plt.plot(nilai_x, u_akhir[55,:], label='t=0.55s')
plt.plot(nilai_x, u_akhir[80,:], label='t=0.8s')
plt.plot(nilai_x, u_akhir[99,:], label='t=1s')
plt.grid()
plt.ylim(-1, 1)
plt.xlim(0,1)
plt.legend()
plt.show()