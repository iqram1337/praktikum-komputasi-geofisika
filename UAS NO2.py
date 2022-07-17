"""
Iqram Haris Fahromi
12320021 / Teknik Geofisika
"""
import numpy as np
import matplotlib.pyplot as plt

k = 0.3  ## ini optional pak, bingung di soal nggk dikasih tau :D           
dt = 0.01                    
dx = 0.2              
t = np.arange(0, 6)     
x = np.arange(10, 20)                 

diskrit_t = int(len(t)/dt)

diskrit_x = int(len(x)/dx)+1


Tu = np.zeros(diskrit_x)
Tu[0] = 0                  
Tu[20] = 100             

for u in range(1, diskrit_t-1):
    for v in range(1, diskrit_x-1):
        Tu[v] = Tu[v] + (dt*k)/(dx**2) * (Tu[v-1] - 2*Tu[v] + Tu[v+1])


plt.grid()
plt.plot(Tu)
plt.title(r'$ \alpha = $ {}'.format((dt*k)/(dx**2)))
plt.show()