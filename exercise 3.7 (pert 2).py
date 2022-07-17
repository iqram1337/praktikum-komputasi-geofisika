## frequency of random numbers
import random

n = int(input('masukkan N: '))

m = 0
for i in range(1, n+1, 1):
    data = random.randint(1, 6)
    print('data random :', data)
    if data == 6:
        m +=1
    else:
        pass
print('')

print('M :', m)
print('N :', n)
print('answer :', m/n)