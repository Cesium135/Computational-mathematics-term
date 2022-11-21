

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 20)
y=((1+2*(x**2))/(1+(x**2)))**0.5
z=(1+x)/(2+(np.cos(x))**3)

fig, axs = plt.subplots(2)
fig.suptitle("Графики функций y=((1+2x^2)/(1+x^2))^0.5 и z=(1+x)/(2+cos((x))^3")
axs[0].plot(x, y,label='((1+2x^2)/(1+x^2))^0.5')

axs[1].plot(x, z,label='(1+x)/(2+cos((x))^3')
plt.xlabel("x")
plt.ylabel("y")

plt.show()