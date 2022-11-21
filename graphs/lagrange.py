
import numpy as np 
import matplotlib.pyplot as plt
import scipy.interpolate as scint
x=[-2,-1.3,-0.7,-0.1]
y=[10.643,4.6305,-1.77810,-7.9772]

flagrange=scint.lagrange(x,y)
xs=np.linspace(-2,5,50)
print('многочлен лагранжа:',flagrange)
print('значения многочлена в точках 1,2,3,4,5',flagrange([1,2,3,4,5]))
plt.plot(xs,flagrange(xs))
plt.show
