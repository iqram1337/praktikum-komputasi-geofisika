import numpy as np
import matplotlib.pyplot as plt

f = lambda x : 1/(x+1)
a = 0
b = 1 
n = 100

### formula
x = np.linspace(a,b,n+1)
y = f(x)

ans = 0
for i in range(len(x)-1):
    ans +=0.5*((x[i+1]) - x[i]) * (y[i+1] + y[i])
print(ans)


### Grafik
sumbu_x = np.linspace(a,b,100)
sumbu_y = f(sumbu_x)
plt.plot(sumbu_x, sumbu_y, label = r'$\int_0^1 \sqrt{x} \mathit{dx}$')

for i in range(n):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='r',alpha=0.2)

plt.title('Trapezoid Rule, N = {}'.format(n))
plt.legend()
plt.show()