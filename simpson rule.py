import numpy as np
import scipy.integrate as spi

## cara singkat
N = 2
a = 0
b = 1


x = np.linspace(a,b,N+1)

y = np.sqrt(x)

print(x)

ans = spi.simps(y,x)

print(ans)