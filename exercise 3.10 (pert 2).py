f""""
Group 6
Nadya Cindy Putri / 12320019
Ahmad Muchamad Zainulwafa / 12320020
Iqram Haris Fahromi / 12320021
"""
import random

data = random.sample(range(1, 10), 6)
print('data :', data)

storage = 0
for i in range (len(data)-1, 0, -1):
    for j in range(i):
        if data[j] > data[j+1]:
            storage = data[j]
            data[j] = data[j+1]
            data[j+1] = storage

print('data :', data)