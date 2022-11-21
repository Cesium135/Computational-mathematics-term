import numpy as np 
import scipy.integrate as scigr
def func(x):
    return 1/np.sqrt(13*x**2-1)

def const(s,n):
    amount=n
    if s=='left':
        k=[1]*amount
        k.append(0)
        return k
    elif s=='right':
        k=[1]*amount
        k.insert(0,0)
        return k
    
a=0.5
b=1.5
n=10
step=(b-a)/n
fres=[func(a+step*i) for i in range(n)]
fresp=[func(a+(step/2)*i) for i in range(n)]
print('решение трапециями:',scigr.trapezoid(fres,x=None,dx=step))
print('решение симпсоном:',scigr.simpson(fres,x=None,dx=step))
l=const('left',n)
r=const('right',n)
print('решение левыми прямоугольниками:',step*(sum([fres[i]*l[i] for i in range(n)])))
print('решение правыми прямоугольниками:',step*(sum([fres[i]*r[i] for i in range(n)])))
print('решение средними прямоугольниками',step*sum(fresp))
