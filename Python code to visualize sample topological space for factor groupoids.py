import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

theta = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(figsize=(30, 100), dpi = 300)

x1 = np.cos(theta)
x2 = np.sin(theta)

ax.plot(x1, x2, linewidth = 0.5)

#Below, m is the number of steps, w is the horizontal shift, z is the vertical shift, u is the contracting factor, and
#v is the rotation angle (in radians).

def corona(m, w, z, u, v):
    n = 1
    while n < m:
        r = 0.5**n
        s = 0.5**n
        t = 0.5**n
        for k in np.arange(0,2**n):
            x = np.cos(v)*u*(r*np.cos(theta) + (1 + 2*s)*np.cos(2*np.pi*((2*k + 1)*t))) - np.sin(v)*u*(r*np.sin(theta) + (1 + 2*s)*np.sin(2*np.pi*((2*k + 1)*t))) + w
            y = np.sin(v)*u*(r*np.cos(theta) + (1 + 2*s)*np.cos(2*np.pi*((2*k + 1)*t))) + np.cos(v)*u*(r*np.sin(theta) + (1 + 2*s)*np.sin(2*np.pi*((2*k + 1)*t))) + z
            ax.plot(x, y, linewidth = 0.5)
        n = n + 1

corona(8, 0, 0, 1, 0)

corona(8, -2, 0, 0.5, 0)

corona(8, 0, -1.5, 0.25, np.pi/2)

corona(8, 0, 1.5, 0.25, 3*np.pi/2)

corona(8, 0, 2, 0.125, 3*np.pi/2)

corona(8, (0.5**0 + 0.5**1)*(0.5**2), 0.5**0 + 0.5**1, 0.5**4, np.pi)

def selfsimilar(m):
    n = 2
    while n < m:
        for k in np.arange(0, 2**n):
            corona(8, (1 + 0.5**n)*np.cos((2*k + 1)*np.pi/(2**n)), (1 + 0.5**n)*np.sin((2*k + 1)*np.pi/(2**n)), 0.5**(n + 1), ((2*(k + 2**(n - 1)) + 1)*np.pi)/(2**n))
        n = n + 1

selfsimilar(6)
        
ax.set_aspect(1)

plt.xlim(-4,1.75)
plt.ylim(-2.5,2.5)

plt.grid(linestyle='--')

plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

plt.show()