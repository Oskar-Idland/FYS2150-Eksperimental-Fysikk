import pandas as pd 
import os 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
filepath = os.path.dirname(__file__)

data = pd.read_csv(os.path.join(filepath, 'faraday.csv'))
print(data.head())
B = data['B'].values
θ = data['theta'].values

L = 30
result = linregress(θ, B)
a = result.slope
b = result.intercept

plt.plot(θ, a*θ + b)
# plt.show()
print(f'b = {b: .4g}')
print(f'a = {a: .4g}')

f = 10
ε = np.sqrt(1 - 1/f**2)
z = f + np.sqrt(f**2 - 1)
# D_par = (1 - 1/ε**2)*(1 - 1/(2*ε)*np.log((1 + ε)/(1 - ε)))
D_par = 1/(1 - f**2)*(1 - f/(np.sqrt(f**2 - 1))*np.log((f + np.sqrt(f**2 - 1))))
print(D_par)