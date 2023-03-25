import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
plt.rcParams.update({'errorbar.capsize': 1})

f_m = 11497.37516787
c = 331.1
f = 11500.425
v = c*(1 - f/f_m)
print(f'v: {abs(v): .2g} m/s')

f_målt = np.array([11498.90123306, 11498.90123306, 11498.90123306, 11498.90123306,                  11498.90123306,       11498.90123306, 11498.90123306, 11498.90123306, 
                
                11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 11497.37516787, 
                
                11495.84910267, 11495.84910267, 11495.84910267, 11500.42729825, 11500.42729825])

print(f'{10*25000/16}')
print(f'Frekvensoppløsning: {25000/15625.0}')
print(f'Tidsoppløsning: {15625.0/25000}')

print(np.std(f_målt)*c / f_m)




# f1γ1 = np.array([11497.37416787, 11494.32303748, 11485.16664632, 
            #    11472.95812437, 11457.69747284])
            
f1γ1 = np.array([11489.90123306, 11474.48418996, 11459.22353803])
t1γ1 = np.linspace(0, 1.75, len(f1γ1))

f2γ1 = np.array([11494.32303748, 11485.16664632, 11472.95812477]) # 11460.74960322, 11451.59321206
t2γ1 = np.linspace(0, 1.89, len(f2γ1))

f3γ1 = np.array([11497.37516767, 11491.27090709, 11476.010225516]) # 11463.80173361, 11454.64534245
t3γ1 = np.linspace(0, 1.9, len(f3γ1))



f1γ2 = np.array([11493.10218533, 11482.11451593, 11467.46429007]) # 11456.47662067, 11445.48895129
t1γ2 = np.linspace(0, 1.52, len(f1γ2))

f2γ2 = np.array([11312.72127945, 11303.56488829, 11294.40849713]) # 11285.25210597, 11276.09571481, 11266.93932365
t2γ2 = np.linspace(0, 1.32, len(f2γ2))

f3γ2 = np.array([11495.84910267, 11486.69271151, 11477.53632035]) # 11468.37992919, 11459.22353803, 11450.06714687, 11440.91075571
t3γ2 = np.linspace(0, 1.53, len(f3γ2))

v1γ1 = c*(1 - f/f1γ1)
v2γ1 = c*(1 - f/f1γ2)
v3γ1 = c*(1 - f/f1γ2)

v1γ2 = c*(1 - f/f2γ1)
v2γ2 = c*(1 - f/f2γ2)
v3γ2 = c*(1 - f/f2γ2)

tγ1 = (t1γ1 + t2γ1 + t3γ1)/3
tγ2 = (t1γ2 + t2γ2 + t3γ2)/3

vγ1 = (v1γ1 + v2γ1 + v3γ1)/3
vγ2 = (v1γ2 + v2γ2 + v3γ2)/3

resγ1 = linregress(tγ1, vγ1)
resγ2 = linregress(tγ2, vγ2)


αγ1, βγ1 = resγ1.slope, resγ1.intercept
αγ2, βγ2 = resγ2.slope, resγ2.intercept
σγ1 = resγ1.stderr
σγ2 = resγ2.stderr


# plt.figure(figsize=(5.8, 8.3)) 
# plt.plot(t, α*t + β, label=r'Lineær regresjon')
# plt.scatter(t, v)
# plt.title('Lineær regresjon av hastighet')
# plt.legend([r'v_1'])
# plt.savefig('Linreg.pdf')
# plt.show()

plt.figure(figsize=(5.8, 8.3)) 
plt.plot(tγ1, αγ1*tγ1 + βγ1, label= r'γ_2')
plt.scatter(tγ1, vγ1)

plt.plot(tγ2, αγ2*tγ2 + βγ2, label=r'γ_1')
plt.scatter(tγ2, vγ2)
plt.legend()
plt.title(r'Lineær regresjon av hastighet')
plt.show()


print(f'αγ1: {αγ1: .3g}   σγ1: {σγ1: .3g}')
print(f'αγ2: {αγ2: .3g}   σγ2: {σγ2: .3g}')

def a_t(θ):
    return 9.81*np.sin(np.deg2rad(θ))

θ = np.linspace(0, 10, 100)
γ1 = 5.106 # degrees
γ2 = 6.907 # degrees
a_teoretisk = a_t(θ)
plt.plot(θ, a_teoretisk, label=r'Teoretisk akselerasjon')
plt.scatter(γ1, αγ1, label=r'Målt akselerasjon ved $γ_1$')
plt.scatter(γ2, αγ2, label=r'Målt akselerasjon ved $γ_2$')
plt.errorbar(γ1, αγ1, σγ1, capsize=20, elinewidth=3)
plt.errorbar(γ2, αγ2, σγ2, capsize=20, elinewidth=3)
plt.show()


# v = np.append(v1, v2, v3)
# print(v)
# print(f'avg: {(np.average(v))}')