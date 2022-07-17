#METODE SIMPSON 1/3
#Muhammad Zaky Ramadhani
#NIM 12320008

#Definisi fungsi 
import numpy as np
def f(x):
     return (1/(x+1)) #SOAL INTEGRALNYA

a = 0 #batas bawah
b = 1 #batas atas
n = 10000 #banyaknya data yg ingin dipartisi
h = (b-a)/n
x = np.linspace (a, b, n)

#sum integrasi
sum_genap = 0
sum_ganjil = 0
for i in range(1, n-1):
    if np.mod(i,2) == 0: #Pembagian 2 sisa 0 = dilihat yg genap
        sum_genap = sum_genap + 2*f(x[i])
    else:
        sum_ganjil = sum_ganjil + 4*f(x[i])

#Hasilnya adalah
Hasil = (h/3)*(f(a)+sum_ganjil+sum_genap+f(n))
print('Hasil Integral = ', Hasil)
    