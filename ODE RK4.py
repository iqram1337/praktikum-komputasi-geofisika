import numpy as np
import matplotlib.pyplot as plt

N = 100
t = np.linspace(1, 2, N)
T = np.zeros(N)

T[0] = 0.5
h = 0


T_err = 0.5*np.exp(0.5*(t**2))

fungsi = lambda T, t: t*T
for i in range(N-1):
    h = t[i+1] - t[i]

    k1 = h*fungsi(t[i], T[i])
    k2 = h*fungsi(t[i] + (0.5*h), T[i] + (0.5*k1))
    k3 = h*fungsi(t[i] + (0.5*h), T[i] + (0.5*k2))
    k4 = h*fungsi(t[i+1], T[i] + k3)

    T[i+1] = T[i] + (1/6*(k1+k2+k3+k4))

trun_error = abs(T_err-T)

print(len(T))
plt.plot(t, T, label = 'Runge-Kutta orde 4')
plt.plot(t, trun_error, label = 'Trun Error')
plt.grid()
plt.legend()
plt.show()