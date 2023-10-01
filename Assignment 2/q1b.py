import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def y(x):
    y = np.sin(5*x) + np.cos(11*x)
    return y

t = np.arange(0, 14.05, 0.05)
# print(t)

# create pandas dataframe object
df = pd.DataFrame({
    'time (t)': t, 
    'y(t)': y(t)}
)

# print(df.head(10))

# get moving average for 10, 4, and 30 units, respectively
nums = [10, 4, 30]
for n in nums:
    df[f'{n}MA'] = df['y(t)'].rolling(n, 1).mean()

# print(df.head(10))

# plotted the graphs
plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(df['time (t)'], df['y(t)'])
plt.xlabel('Time, t (s)')
plt.ylabel('y(t)')

plt.subplot(3, 1, 2)
plt.plot(df['time (t)'], df['4MA'])
plt.xlabel('Time, t (s)')
plt.ylabel('4 Measurement MA')

plt.subplot(3, 1, 3)
plt.plot(df['time (t)'], df['30MA'])
plt.xlabel('Time, t (s)')
plt.ylabel('30 Measurement MA')

# plt.savefig('Assignment 2\Q1b - Graph')
plt.show()