import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 12*x**2+3*x-5

e=0.01
x=np.linspace(-5,5,50)
y=f(x)
plt.plot(x,y) #минимум функции в интервале [1,1]
a=-1
b=1
print('решение методом золотого сечения')
z=(3-(5**0.5))/2
x1=a+z*(b-a)
dx1=b-z*(b-a)
f1,df1=f(x1),f(dx1)
while b-a>2*e:
    if f1<df1:
        b,dx1,df1=dx1,x1,f1
        x1=a+z*(b-a)
        f1=f(x1)
    else:
        a,x1,f1=x1,dx1,df1
        dx1=b-z*(b-a)
        df1=f(dx1)
resx=(a+b)/2
print('минимум функции находится в точке',resx,
      '\nфункция равна', f(resx))

print('решение методом деления на три отрезка')
a,b=-1,1
x1,x4=a,b

while x4-x1>2*e:
    x2=x1+(x4-x1)/3
    x3=x4-(x4-x1)/3
    f2,f3=f(x2),f(x3)
    if f2<f3:
        x4=x3
    else:
        x1=x2
res=(x1+x4)/2
print('минимум функции находится в точке',res,
      '\nфункция равна', f(res))

print('решение методом половинного деления')
x1,x4=a,b
while x4-x1>2*e:
    x2=(x4+x1)/2
    x3=x2+(x4-x1)/100
    f2,f3=f(x2),f(x3)
    if f2<f3:
        x4=x3
    else:
        x1=x2
ress=(x1+x4)/2
print('минимум функции находится в точке',ress,
      '\nфункция равна', f(ress))
plt.plot(resx,f(resx),'o')
plt.show()