import numpy as np

nn = 100
data = np.random.random(nn)
n_data = len(data)

total = 0
for i in range(0, n_data):
    total = total + data[i]

mean = total/n_data
print(mean)