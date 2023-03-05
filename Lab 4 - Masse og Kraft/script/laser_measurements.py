import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

weight = np.array([0, 1, 10, 100, 500, 600, 700, 1000, 1100, 1200, 1500, 1600, 1700, 2000, 2100, 2110, 2120, 2130, 2131])  # g
d_laser = np.array([0, 0.2, 0.5, 4.4, 23.2, 27.8, 32.4, 46.0, 50.3, 54.8, 67.7, 72.1, 76.1, 89.0, 92.9, 93.3, 93.7, 94.2, 94.3]) # Measured deformation in cm
d_alu = np.array([95.7, 95.7, 95.7])  # Measured deformation with aluminium weight

def line(x, y):
    fit = stats.linregress(x, y)
    a = fit.slope
    b = fit.intercept
    σ_a = fit.stderr
    σ_b = fit.intercept_stderr
    return a, b, σ_a, σ_b

def mean(data):
    """
    finner gjennomsnitt
    """
    f = 1 / len(data) * np.sum(data)
    return f


def std(data):
    """
    Finner standardavvik
    """
    f = mean(data)
    s = np.sqrt(1 / (len(data) - 1) * np.sum((data - f) ** 2))
    return s


def mean_std(data):
    """
    Finner standardavviket i gjennomsnittet
    """
    return std(data) / np.sqrt(len(data))



Δl = (0.001**2 + 0.01**2 + mean_std(d_alu)**2)**0.5

a1, b1, σ_a1, σ_b1 = line(d_laser, weight)
print("LASER")
print('-----')
print(f"a: {a1:.4g}")
print(f"b: {b1:.4g}")
print(f"σ a: {σ_a1:.4g}")
print(f"σ b: {σ_b1:.4g}")
print(f'Δl: {0.707: 4f} cm')
print(f'm: {95.7*a1 + b1: 4f} g') 
print(f'Δm: {((95.7*σ_a1)**2 + (a1*Δl)**2 + b1**2)**0.5: 4f} g')
plt.figure(figsize=(16,9))
fontsize = 22
plt.scatter(d_laser, weight)
plt.plot(d_laser, (a1*d_laser + b1))
plt.xlabel(r"$δl$ [cm]", fontsize = fontsize)
plt.ylabel("Weight [g]", fontsize = fontsize)
plt.grid()
plt.savefig("C:/Users/oskar/OneDrive - Universitetet i Oslo/Dokumenter/GitHub/Privat/FYS2150-Eksperimental-Fysikk/1 Lab Raport/fig/linreg_laser.pdf")
plt.show()
