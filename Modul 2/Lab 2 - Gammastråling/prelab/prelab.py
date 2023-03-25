import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os 
filepath = os.path.dirname(__file__)

with open(os.path.join(filepath, 'poisson.csv'), 'r') as f:
    data = []
    for line in f:
        data.append(int(line))
    
    data = np.array(data)

mean = np.mean(data)
σ = np.std(data)
print(f'mean = {mean: .2f}, σ = {σ: .2g}')


skjerming = np.array([0, 4, 8, 12, 16, 20, 24])
n = np.array([13.7, 12.4, 11, 9.7, 8.9, 7.9, 7.1])
plt.scatter(skjerming, n, color = 'red')
result = linregress(skjerming, n)
svekkningskoeffisient, b = result.slope, result.intercept
plt.plot(skjerming, svekkningskoeffisient*skjerming + b)
# plt.show()
plt.close()
print(f'svekkningskoeffisient = {svekkningskoeffisient*1000: .4g} / m, std = {result.stderr*1000: .4g} / m')


I_0 = 13.7

z = -np.log(0.05) / 275
print(f'z = {z*1000: .2f} m for å få 5% av intensiteten')

with open(os.path.join(filepath, 'spektrum.csv'), 'r') as f:
    data = []
    f.readline()
    for line in f:
        data.append(float(line))
    
data = np.array(data)
plt.plot(data)
# plt.show()
print(np.mean(data), np.std(data))

data = pd.read_csv('spektrum.csv')
print(f'mean = {data["spektrum"].mean()}, σ = {data["spektrum"].std(ddof=0)}, median = {data["spektrum"].median()}')
print(data.describe())
data.plot(y='spektrum')
print(data)
plt.show()