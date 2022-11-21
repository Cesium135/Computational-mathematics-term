import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sqrt(0.16-(x/3)**2)+x
def df(x):
    return np.sqrt(-2*x)/3+x
x1=-0.5
beta=(-2/df(x1))
print(beta)
for i in range(10):
    print(x1)
    x1+=f(x1)*beta
x=np.linspace(-1.2,1.2,50)
z=x*0
print(x1)
plt.plot(x,f(x))
plt.plot(x,z)
plt.plot(-0.3795,f(-0.3795),'o')
plt.show()
