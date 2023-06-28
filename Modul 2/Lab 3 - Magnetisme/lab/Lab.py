import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os 
filepath = os.path.dirname(__file__)

def sig_dig(v, u):
    
    if u > v:
        return 'Uncertainty is greater than value dumbo'
    
    if u == 0:
        return 'Uncertainty is zero, sure this is correct?'
    
    elif u > 1:
        u = str(u).split('.')[0]
        rounding_digit = len(u) 
        multiplier = 10**-(rounding_digit)
        return np.floor(v*multiplier + 0.5)/multiplier

    elif 'e' in str(u) or 'E' in str(u):
        decimal_places = int(str(u)[-2:])
        return round(v, decimal_places)

    else:
        decimal_places = len(u) - len(u.lstrip('0')) + 1
        return round(v, decimal_places)
    



# Oppgave 1
As = np.pi*(np.array([10.33, 10.25, 10.20]) / 100 / 2)**2 # m
A = np.mean(As)
print('Oppgave 1\n')
print(f'A = {sig_dig(A,np.std(As))} ± {np.std(As):.1}')

μ_0 = 4*np.pi*10**(-7)
I = np.arange(0, 2.5, 0.2)
B1 = 0.001*np.array([26.0, 98.3, 177.7, 262.0, 344.8, 420.0, 493.0, 560.1, 620.2, 676.4, 724.4, 765.3, 802.9])  # B1 without Vismuth
B2 = 0.001*np.array([0.0, 0.3, 0.8, 1.4, 1.9, 2.3, 2.6, 2.9, 3.1, 3.2, 3.3, 3.4, 3.4])  # B2 with Vismuth
m = 0.001*np.array([0.00, 0.00, 0.00, 0.02, 0.05, 0.08, 0.11, 0.16, 0.19, 0.22, 0.25, 0.28, 0.31])
fz = 9.81*m

x     = -2*μ_0*fz/(A*((B1**2)-(B2**2))) # Beregner susceptibiliteten
x_alt = -2*μ_0*fz/(A*(B1**2))           # Beregner alternativ susceptibilitet

print('Susceptibilities:')
print(f'X     = {sum(x)/len(x): .3}')
print(f'X_alt = {sum(x_alt)/len(x_alt): .3}')
print('------------------------------------')

# # Oppgave 2
puck_par =   6.88 * 10**-3   # m
puck_ort =  59.91 * 10**-3   # m

kule_par =  63.5  * 10**-3   # m
kule_ort =  63.5  * 10**-3   # m

spyd_par = 208    * 10**-3   # m
spyd_ort =  10    * 10**-3   # m

stav_par =  64.6  * 10**-3   # m
stav_ort =  10    * 10**-3   # m

def D(a_par, a_ort):
    f = a_par / a_ort
    
    if a_par == a_ort:
        D_par =  1/3
    
    elif f > 1:
        D_par =  1/(1 - f**2)*(1 - f/np.sqrt(f**2 - 1)*np.log(f + np.sqrt(f**2 - 1)))
        
    else:
        D_par = 1/(1 - f**2)*(1 - f/(np.sqrt(1 - f**2))*np.arccos(f))
        
    D_ort = (1 - D_par)/2
    return D_par, D_ort


puck_D_par, puck_D_ort = D(puck_par, puck_ort)
kule_D_par, kule_D_ort = D(kule_par, kule_ort)
spyd_D_par, spyd_D_ort = D(spyd_par, spyd_ort)
stav_D_par, stav_D_ort = D(stav_par, stav_ort)

print('Oppgave 2\n')
print(f'Puck: D_par = {puck_D_par: .3f}, D_ort = {puck_D_ort: .3f}')
print(f'Kule: D_par = {kule_D_par: .3f}, D_ort = {kule_D_ort: .3f}')
print(f'Spyd: D_par = {spyd_D_par: .3f}, D_ort = {spyd_D_ort: .3f}')
print(f'Stav: D_par = {stav_D_par: .3f}, D_ort = {stav_D_ort: .3f}')
print('------------------------------------')

# # Oppgave 3
I1 = np.array([0.68, 1.71, 2.74, 3.83, 4.93, 5.89, 6.71])
S1 = np.array([41.13, 524.42, 529.56, 565.55, 611.83, 745.5, 853.47])
I2 = np.array([1.44, 2.53, 3.56, 4.66, 5.82, 6.71, 7.53])
S2 = np.array([174.81, 1038.56, 1377.89, 1619.54, 1789.2, 1989.72, 2133.68])
k = 1.01 * 10**-6
D = 10
n = 130
A = np.pi*(6.5/2 * 10**-3)**2

B = k*D*(S2 - S1)/(2*n*A)
I = (I1 + I2)/2

plt.plot(I, B, label='B(I)')
plt.legend()
plt.savefig(os.path.join(filepath, 'Oppgave 3 - B(I).pdf'))
plt.show()

N = 344
L = 315 * 10**-3
H0 = N*I/L
X = 1.66 * 10**-4
μ_0 = 4*np.pi*10**-7
M = B/(μ_0) - H0
plt.plot(H0, M, label=r'M(H_0)')
plt.legend()
plt.savefig(os.path.join(filepath, 'Oppgave 3 - M(H0).pdf'))
plt.show()


# # Oppgave 4

print('Oppgave 4\n')
I = np.array([-3, -2.5, -2, -1.5, -1, 0,  1,  1.5,  2,  2.5,  3])
B = np.array([-119, -102, -83, -63, -43, 0, 43, 63, 83, 102, 119]) / 1.5 / 1000

θ_red = np.array([-5, -4, -3, -3, -2, 0,  1,  2,  3,  3,  4])
θ_green = np.array([-7, -6, -5, -4, -3, 0,  2,  3,  5,  5,  7])

red_slope, red_intercept = linregress(B, θ_red)[:2]
green_slope, green_intercept = linregress(B, θ_green)[:2]
print(f'Red Verdet constant: {red_slope: .3f}')
print(f'Green Verdet constant: {green_slope: .3f}')
print(f'Red uncertainty in Verdet constant: {linregress(B, θ_red).stderr: .3f}')
print(f'Green uncertainty in Verdet constant: {linregress(B, θ_green).stderr: .3f}')

plt.plot(B, B*red_slope + red_intercept, label='red', color = 'red')
plt.scatter(B, θ_red, label='red data', color = 'orange')
plt.plot(B, B*green_slope + green_intercept, label='green', color = 'green')
plt.scatter(B, θ_green, label='green data', color = 'blue')
plt.legend()
plt.title('Lineær regresjon av vinkel mot magnetfelt')
plt.savefig(os.path.join(filepath, 'Oppgave4.pdf'))
plt.show()