import numpy as np 
import matplotlib.pyplot as plt

xx = np.linspace(0, 10, 100)
x0 = 5
x1 = (xx-x0)**2
y1 = np.exp(-0.5*x1)

# shifted gaussian
x2 = (xx-x0-1)**2
y2 = np.exp(-0.5*x2)

plt.plot(xx, y1, 'r-', xx, y2, 'b-')
plt.legend(['f(x) = exp(-0.5*(x-5)**2)', 'f(x-1)'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()