""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
import numpy as np
import matplotlib.pyplot as plt

ds = 0.1
N = 600
p = np.zeros(2)
dp = np.zeros(2)
xz = np.zeros(2)
thet = 45
v0 = 2
p[0] = np.cos(np.deg2rad(thet)/v0)
p[1] = np.sin(np.deg2rad(thet)/v0)
xz[0] = 0
xz[1] = 0

dv = 0.1
dp[0] = 0
dp[1] = -dv/(v0**2)


T = np.exp(0.5*(p**2))

v = v0
grafik_xz = []

f = lambda p, v: p*v
for i in range(N-1):
    k1 = ds*f(p, v)
    k2 = ds*f(p + (0.5*ds), v + (0.5*k1))
    k3 = ds*f(p + (0.5*ds), v + (0.5*k2))
    k4 = ds*f(p, v + k3)

    xz = xz + (1/6*(k1 + k2 + k3 + k4))
    p = p + (dp)*ds
    v = v0 + dv*xz[1]

    dp[1] = -dv/(v**2)

    grafik_xz = np.append(grafik_xz, xz)

grafik_xz = np.reshape(grafik_xz, (N-1, 2))
T_err = abs(T - grafik_xz)

plt.ylim(15, 0)

plt.plot(grafik_xz[:, 0], grafik_xz[:, 1], color = 'blue', label = 'Ray Tracing')
plt.plot(T_err, T_err, color = 'red', label = 'np.exp(0.5*(p**2))')

plt.ylabel('depth', color = 'orange')
plt.xlabel('n', color = 'orange')

plt.legend()
plt.grid()
plt.show()



