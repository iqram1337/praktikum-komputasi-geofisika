import numpy as np

x = np.linspace(0, 2, 3)
print(f"arr x = {x}")

y = np.copy(x)              # men-copy data x ke y
print(f"arr y = {y}")
print('')                   # spasi biasa
print('arr y[0] =', y[0])   # print data y ke-0

y[0] = 99                   # mengganti suku nilai dari data y
print('arr y[0] =', y[0], '(setelah diganti)')   # print data y ke-0 yg baru
print('')

# print hasil akhir
print(f"arr y = {y}         (berubah)")
print(f"arr x = {x}         (tak berubah)")

