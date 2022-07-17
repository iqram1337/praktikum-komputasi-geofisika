import numpy as np

f""""
rumus = ((b-2)/2) * [w1*f(x1) + w2*f(x2)]

"""
def f(x):
    fx = np.sqrt(x)           #YG DIUBAH
    return fx
a = 0
b = 1
w1 = w2 = 1
z1, z2 = -1/(np.sqrt(3)), 1/(np.sqrt(3))

x1 = ((b-a)/2)*z1 + ((b+a)/2)
x2 = ((b-a)/2)*z2 + ((b+a)/2)


ans =  ((b-a)/2) * ((w1*f(x1)) + (w2*f(x2)))
print(ans)

