import numpy as np
def f1(x):
    return np.sqrt(0.16-(x[0]/3)**2)+x[1]
def f2(x):
    return np.cos(x[0])+x[1]-0.5
def df1(x):
    return -5*x[0]/(3*np.sqrt(36-25*(x[0]**2)))
def df2(x):
    return -np.sin(x[0])

x0=np.array([[0.3],[0.3]])

for i in range(10):
    j=np.array([[df1(x0)[0],1],[df2(x0)[0],1]])
    jobr=np.linalg.inv(j)
    fres=np.array([[f1(x0)[0]],[f2(x0)][0]])
    ressave=x0
    x0=x0-np.dot(jobr,fres)
    dxn=np.linalg.norm(x0-ressave)
    if dxn<0.01:
        break
print(x0)