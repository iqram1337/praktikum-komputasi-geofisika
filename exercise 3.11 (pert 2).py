f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
import numpy as np
import matplotlib.pyplot as plt

n = int(input('Masukkan N: '))
print('----------------------------------------------------------')

## cara leibniz
leibniz_error = []
for i in range(n):
    leibniz_error.append(0)
hasil1 = 0

for i in range(n-1):
    hasil1 = hasil1 + (1/((4*i)+1)) * (1/((4*i)+3))
    leibniz_error[i+1] = np.pi - 8*hasil1
hasil1 = 8*hasil1

print('Metode Leibniz :', hasil1)
print('Leibniz error  :', np.abs(np.pi-hasil1))
print('')


## cara Euler
euler_error = []
for i in range(n):
    euler_error.append(0)
hasil2 = 0

for i in range(1, n):
    hasil2 = hasil2+(1/(i**2))
    euler_error[i] = np.pi - np.sqrt(6*hasil2)
hasil2 = np.sqrt(6*hasil2)

print('Metode Euler :', hasil2)
print('Euler error  :', np.abs(np.pi-hasil2))


## ploting grafik error Leibniz dan Euler
sumbu_x = [i for i in range(n)] #list comprehension
plt.title('Compute PI')
plt.plot(sumbu_x, leibniz_error, 'g-', label = 'Leibniz')
plt.plot(sumbu_x, euler_error, 'b--', label = 'Euler')

plt.xlabel('N', color = 'red')
plt.ylabel('Leibniz & Euler Error', color = 'red')

plt.legend()


plt.show()