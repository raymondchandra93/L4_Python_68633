import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
x = np.sin(7*t*np.pi)
y = np.sin(5*t*np.pi)

fig = plt.figure()
plt.plot(x, y)
fig.savefig("lissajous2")