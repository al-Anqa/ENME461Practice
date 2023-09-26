import scipy.fft
import numpy as np
import matplotlib.pyplot as plt


t_int = 1/256 #seconds
t = np.arange(0, 1, t_int)
# print(len(t))
eqn = 5 + 2 * np.cos(10 * np.pi * t) + np.sin(20 * np.pi * t) + 3 * np.cos(30 * np.pi * t)

fft = scipy.fft.fft(eqn)
print(fft)
amplitude = max(fft)

plt.plot(t, eqn)
plt.show()