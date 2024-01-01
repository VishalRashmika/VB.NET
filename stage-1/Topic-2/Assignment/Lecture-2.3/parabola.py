import matplotlib.pyplot as plt
import numpy as np
x  = np.linspace(-50,50,100)
y = (x + 5) * (x + 3)

plt.xlim(-10, 4)
plt.ylim(-2, 30)


plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.plot(x,y)
plt.grid()
plt.show()