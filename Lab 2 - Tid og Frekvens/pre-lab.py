import numpy as np
import random
import matplotlib.pyplot as plt

def mean(data):
    """
    finner gjennomsnitt
    """
    f = 1/len(data)*np.sum(data)
    return f


def std(data):
    """
    Finner standardavvik
    """
    f = mean(data)
    s = np.sqrt(1/(len(data)-1)*np.sum((data-f)**2))
    return s

def mean_std(data):
    """
    Finner standardavviket i gjennomsnittet
    """
    return std(data)/np.sqrt(len(data))



data = np.loadtxt("data1.csv")
X = mean(data)
σ = std(data)
X_σ = mean_std(data)

print(f"Midlere verdi: {X: .3g}")
print(f"Standardavvik: {σ: .3g}")
print(f"Standardavviket til midlere verdi: {X_σ: .3g}")
print(f"Prosent av data innenfor 1 standardavvik: {len(np.where(abs(data - X) <=   σ)[0])/len(data): .0%}")
print(f"Prosent av data innenfor 2 standardavvik: {len(np.where(abs(data - X) <= 2*σ)[0])/len(data): .0%}")



"""
n = np.array([2,20,40,60,80,100,150,250,500,1000])
a = 1
b = 2
xmid = np.zeros(len(n))
s = np.zeros(len(n))
sm = np.zeros(len(n))

random.seed(1)
for i in range(len(n)):
    x = a+b*np.random.randn(n[i],1)
    xmid[i] = mean(x)
    s[i] = std(x)
    sm[i] = mean_std(x)

plt.style.use("seaborn")
plt.plot(n,xmin,label="Gjennomsnitt")
plt.plot(n,s,label="Standardavvik")
plt.plot(n,sm,label="Standardavviket i gjennomsnittet")
plt.legend()
plt.show()
"""