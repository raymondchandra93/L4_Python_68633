import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(2*t)
y = np.sin(3*t)

fig = plt.figure()
plt.plot(x, y)
fig.savefig("lissajous1")