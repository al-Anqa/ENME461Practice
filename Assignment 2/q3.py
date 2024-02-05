import numpy as np
import matplotlib.pyplot as plt


def input_signal(t):
    y = 10 * np.sin(15.7 * t)
    return y

def output_signal(t):
    y = 4.857**(-1 * t / 0.05) + 7.866 * np.sin(15.7 * t + 0.666)
    return y

t = np.arange(0, 5.05, 0.05)

o_fft = np.fft.fft(output_signal(t))
freq = t * np.pi
o_freq = np.fft.fftfreq(len(t), d=1/0.05)[:len(t)//2]

plt.plot(o_freq, 2.0/len(t) * np.abs(o_fft[0:len(t)//2]))
plt.show()