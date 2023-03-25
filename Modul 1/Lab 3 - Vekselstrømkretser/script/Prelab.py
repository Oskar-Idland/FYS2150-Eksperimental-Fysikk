import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os 
filepath = os.path.dirname(__file__)

ω = []
V = []

with open(os.path.join(filepath, 'RC_data.csv')) as f:
    data = f.readlines()
    for line in data[1:]:
        line = line.split(',')
        ω.append(float(line[0]))
        V.append(float(line[1]))

ω = np.array(ω)
V = np.array(V)
anal = linregress(np.log10(ω[-9:]), np.log10(V[-9:]))
slope, ω_0 = anal.slope, anal.intercept
print(f'ω_0 = {(ω_0):.2f}')

plt.yscale('log')
plt.xscale('log')
plt.plot(ω, V)
# plt.show()