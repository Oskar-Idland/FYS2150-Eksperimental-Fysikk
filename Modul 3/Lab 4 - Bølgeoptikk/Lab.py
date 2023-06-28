# TODO: Fiks enheter. Plots stemmer bare hvis jeg setter veldig liten lim. 

import numpy as np 
import matplotlib.pyplot as plt

R = 0.576           # [m] Avstand mellom spalte og skjerm
λ = 632.8 * 1E-9    # [m] Bølgelengden til lyset
π = np.pi


def x(n, λ, R, a):
    return (n*λ*R)/a

def a(n, λ, R, x):
    return (n*λ*R)/x

def E_N(x, R, a, λ, N, A):
    c = 1/(λ*R)
    E1 = np.sinc(a*c*x)**2
    F1 = (np.sin(N*A*c*π*x) / np.sin(A*c*π*x))**2
    if N == 1:
        return E1 
    else:
        return E1 * F1


d_02_1 = 3.15; d_02_2 = 6.20; d_02_3 = 9.40 # [cm]
d_04_1 = 1.60; d_04_2 = 3.00; d_04_3 = 4.70 # [cm]
d_08_1 = 0.80; d_08_2 = 1.50; d_08_3 = 2.35 # [cm]
d_16_1 = 0.35; d_16_2 = 0.75; d_16_3 = 1.20 # [cm]

d_02 = np.array([d_02_1, d_02_2, d_02_3]) * 1E-2 # [m]
d_04 = np.array([d_04_1, d_04_2, d_04_3]) * 1E-2 # [m]
d_08 = np.array([d_08_1, d_08_2, d_08_3]) * 1E-2 # [m]
d_16 = np.array([d_16_1, d_16_2, d_16_3]) * 1E-2 # [m]

for i in range(1, 5):
    d = eval(f'd_{2**i:02}')
    print(f'a: {2**i * 1E-2}mm')
    print('     Eksperiment')
    print('     -----------')
    for n in range(1,4):
        x = d[n-1] / 2
        print(f'    {a(n, λ, R, x)*1E3:>9.4} mm')
    print()
    
a = np.array([0.04, 0.08]) # [mm] Spaltebredde
A = np.array([0.25, 0.50]) # [mm] Avstand mellom spalter
R_mm = R * 1E3             # [mm]
λ_mm = λ * 1E3             # [mm]

lim = 80
x = np.linspace(-lim, lim, 1001) # [mm]


R_mm = 1894
for a_i in a:
    for A_i in A:
        y1 = E_N(x, R_mm, a_i, λ_mm, 1, A_i)
        y2 = E_N(x, R_mm, a_i, λ_mm, 2, A_i)
        plt.plot(x,y1/max(y1), label=r'$E_1(x)$')
        plt.plot(x,y2/max(y2), label=r'$E_2(x)$')
        plt.xlabel('x [mm]', fontsize=18)
        plt.ylabel('E(x) [a.u]', fontsize=18)
        plt.title(f'a = {a_i} mm, A = {A_i} mm', fontsize=18)
        plt.legend(fontsize=18)
        plt.savefig(f'plot_a{a_i}_A{A_i}.pdf')
        plt.show()