f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
import numpy as np
import matplotlib.pyplot as plt

k = 0.8
dt = 0.01
dx = 0.2
t = np.arange(0, 5)
x = np.arange(0, 10)

dis_t = int(len(t)/dt)+1
dis_x = int(len(x)/dx)+1
alp = (dt*k)/(dx**2)

T = np.zeros(dis_x)
T[0] = 100

for u in range(1, dis_t-1):
    for v in range(1, dis_x-1):
        T[v] = T[v] + alp * (T[v-1] - 2*T[v] + T[v+1])


plt.grid()
plt.plot(T)
plt.title(r'$ \alpha = $ {}'.format(alp))
plt.show()