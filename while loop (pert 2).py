import numpy as np
import matplotlib.pyplot as plt

v0 = 4.5
g = 9.81
t = np.linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

print(y)
## while loop
i = 0
while y[i] >= 0:
    i = i +1


plt.plot(t, y)
plt.plot(t, 0*t, 'g--')

plt.xlabel('time')
plt.ylabel('height')

plt.show()