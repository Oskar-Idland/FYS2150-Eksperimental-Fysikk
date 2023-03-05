import numpy as np 
import os 
filepath = os.path.dirname(__file__)

data = np.loadtxt(os.path.join(filepath, "maalinger_deformasjon.dat"))

def line(x,y):
    D = sum(x**2) - 1/len(x) * sum(x)**2
    E = sum(x*y) - 1/len(x) * sum(x)*sum(y)
    m = E/D
    c = sum(y)/len(y) - m*sum(x)/len(x)
    return m, c

x,y = data[:,0], data[:,1]
print(line(x,y))