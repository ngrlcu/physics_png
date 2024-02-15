import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5, 1000)
y = np.sin(7*x)*np.exp(-x**2/4)

plt.xkcd()
plt.figure(figsize=(8,5))

plt.plot(x, y, 'k', linewidth=4)
#plt.arrow(x[-1], y[-1], 0.3, 0, color='k', head_width=0.08, head_length=0.15, linewidth=4, length_includes_head=True)

plt.axis('off')

#plt.show()
plt.savefig("photon.png", dpi=500)
