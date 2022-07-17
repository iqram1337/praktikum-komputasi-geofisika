#Muhammad Zaky Ramadhani
#NIM: 12320008

import numpy as np 

#Definisi fungsi
def f(x):
    return (1/x+1) #SOAL INTEGRALNYA

a = 0
b = 1
n = 100
dx = (b-a)/(n)
x = np.linspace(a, b, n) #vektor dari x

#untuk sum
sum = 0
for i in range (1, n-1):
    sum += f(x[i])

#Hasilnya adalah
Hasil = 0.5*dx*(f(x[a])+2*sum+f(x[n-1]))
print("Hasil Integral Numerik Metode Trapezoidals = ", Hasil)