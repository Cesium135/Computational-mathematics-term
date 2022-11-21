

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 50)
y =( 1.2*((np.e)**x))-x-1.5
plt.title("График функции y=1.2*(sin(x)+2.2)^(cos(x+1)+1.2)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y,label='1.2*(sin(x)+2.2)^(cos(x+1)+1.2)') 
plt.show()
 