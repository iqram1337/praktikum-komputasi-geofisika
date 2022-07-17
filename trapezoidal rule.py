import numpy as np
import matplotlib.pyplot as plt

a = 0                    #YG DIUBAH
b = 1                    #YG DIUBAH               
n = 2                   #YG DIUBAH
h = (b-a)/n

x = np.linspace(a, b, n)
y = np.sqrt(x)          #YG DIUBAH

ans = 0

for i in range(len(x)-1):
    ans +=0.5*((x[i+1]) - x[i]) * (y[i+1] + y[i])

print(ans)


## GRAFIK
sumbu_x = np.linspace(0, 12, 1000)
sumbu_y = np.sqrt(sumbu_x)          #YG DIUBAH

x0 = 0
y0 = np.sqrt(x0)           #YG DIUBAH  
x1 = 1
y1 = np.sqrt(x1)             #YG DIUBAH

plt.plot(sumbu_x, sumbu_y)
plt.fill_between([x0, x1], [y0, y1], alpha = 0.2, edgecolor = 'r')

plt.xlim([-0,1.5])
plt.ylim([0,1.5])
plt.show()


