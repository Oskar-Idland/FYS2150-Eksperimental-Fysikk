import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

weight = np.array([0, 1, 10, 100, 500, 600, 700, 1000, 1100, 1200, 1500, 1600, 1700, 2000, 2100, 2110, 2120, 2130, 2131])  # g
d = np.array([9.28, 9.26, 9.22, 8.84, 7.15, 6.72, 6.26, 4.99, 4.57, 4.12, 2.87, 2.45, 2.01, 0.79, 0.37, 0.30, 0.25, 0.20, 0.20])  # Measured deformation in mm
d_alu = np.array([0.18, 0.15, 0.14, 0.14, 0.13])  # Measured deformation with aluminium weight

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

Δ_l_tot = (0.001**2 + 0.01**2 + mean_std(d_alu)**2)**0.5

a1, b1, σ_a1, σ_b1 = line(d, weight)
print("MÅLEUR")
print('------')
print(f"a: {a1:.4f}")
print(f"b: {b1:.4f}")
print(f"σ a: {σ_a1:.4f}")
print(f"σ b: {σ_b1:.4f}")
print(f"Δl: {Δ_l_tot: .4g} mm")
print(f"m : {a1*(mean(d_alu)) + b1:.4f} g")
Δ_m = np.sqrt((mean(d_alu)*σ_a1)**2 + (a1*Δ_l_tot)**2 + σ_b1**2)
print(f"Δm: {Δ_m:.4g} [g]")

plt.figure(figsize=(16,9))
fontsize = 22
plt.scatter(d, weight)
plt.plot(d, (a1*d + b1))
plt.xlabel(r"$l$ [mm]",fontsize = fontsize)
plt.ylabel("Weight [g]",fontsize = fontsize)
plt.grid()
plt.savefig("C:/Users/oskar/OneDrive - Universitetet i Oslo/Dokumenter/GitHub/Privat/FYS2150-Eksperimental-Fysikk/1 Lab Raport/fig/linreg_maaleur.pdf")
plt.show()