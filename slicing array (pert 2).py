import numpy as np

x = np.arange(1, 15, 2)
print('arr x =', x)

y = x[1:5]          # cuman ngambil data x[1] sampai x[4]
print('arr y =', y)
print('')

y[3] = 99           # mengubah data y ke-3 menjadi 99
print('arr y =', y)
print('')

## hasil akhir
print('arr x =', x, '(tak berubah)')
print('arr y =', y, '(berubah)')
