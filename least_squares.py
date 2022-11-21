import numpy as np
import matplotlib.pyplot as plt
x=np.array([[20],[27],[43],[53],[62],[72],[83],[93],[103],[110]])
y=np.array([[18.38],[21.18],[34.36],[52.04],[81.41],[145],[304],[651],[1521],[2899]])
y2=np.log(y)
fi=np.hstack((x**0,1/x,x**(1/6)))
fit=fi.T
fitfi=fit@fi
fity=fit@y2
a=np.linalg.solve(fitfi,fity)
xx=np.arange(19,115)
yy=np.e**(a[0]+a[1]*(1/xx)+a[2]*(xx**(1/6)))
plt.plot(x,y,'bo',xx,yy,'r-')
print('коэффиценты уравнения регрессии:',a)
