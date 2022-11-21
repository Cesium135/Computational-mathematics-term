import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x[0]**2+x[1]**2+x[0]*x[1]+1.2*x[0]-1.2*x[1]-1
def df1(x):
    return 2*x[0]+x[1]+1.2
def df2(x):
    return 2*x[1]+x[0]-1.2

e=0.01
h=1
x0g=[2,1]
x0s=[2,1]
print('решение градиентным методом')
while h>e:
    fg=f(x0g)
    g=np.array([df1(x0g),df2(x0g)])
    v=(1/np.linalg.norm(g))*g
    z=x0g-np.dot(h,v)
    f2=f(z)
    if f2<fg:
        x0g=z
    else:
        h=h/3
print('минимум функции находится в точке:', x0g,
      '\nзначение в точке минимума:',f(x0g))
print('решение симплексным методом')
h=1
while h>e:
    x1s=[x0s[0],x0s[1]+h]
    x2s=[x0s[0]+h,x0s[1]]
    xs=[x0s,x1s,x2s]
    fx=[f(xs[i]) for i in range(3)]
    for i in range(50):
        bad=fx.index(max(fx))
        fbad=fx.pop(bad)
        xbad=xs.pop(bad)
        xmid=[xs[0][0]+xs[1][0],xs[0][1]+xs[1][1]]
        vs=[xmid[0]*0.5-xbad[0],xmid[1]*0.5-xbad[1]]
        xotr=[xbad[0]+2*vs[0],xbad[1]+2*vs[1]]
        fotr=f(xotr)
        if fotr<=fbad:
            fx.append(fotr)
            xs.append(xotr)
            
        else:
            break
    x0s=xotr
    h=h/3
print('минимум функции находится в точке',x0s,
      '\nзначение функции в точке минимума',f(x0s))
print('разница между симплексным методом и градиентным составила:',np.linalg.norm(x0s)-np.linalg.norm(x0g))

    
    
