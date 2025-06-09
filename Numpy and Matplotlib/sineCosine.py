import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * -1
y4 = np.cos(x) * -1

fig = plt.figure()

plt.plot(x, y1, label='sine')
plt.plot(x, y2, label='cosine')
plt.plot(x, y3, label='inverted sine')
plt.plot(x, y4, label='inverted cosine')

plt.legend()

fig.savefig("sineCosineCurves")