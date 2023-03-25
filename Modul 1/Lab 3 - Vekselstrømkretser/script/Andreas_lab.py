import numpy as np 
from scipy.stats import linregress as sp 
import matplotlib.pyplot as plt 


frekvens = np.array([400,800, 4_000, 8_000, 16_000,32_000, 64_000,128_000,256_000,512_000 ])

likestromsnitt = np.array([10.65,11.24,10.57, 11.16, 11.09,10.8,8.82,6.495,2.31,207*1e-3])


ABrms = np.array([7.535, 7.666, 7.587,7.995,9.011,12.03,18.78,25.61,20.82,5.411])

Arms = np.array([106.2,109.1,107.3,114.8,131,180.2,279.7,473.7,633.2,609.2])

Brms = np.array([100.4,103,100,101.7,99.39,94.88,94.7,76.06,46.25,12.42])

frekvens[-1] = 400_000
Arms[-1] = 639.7
Brms[-1] = 24.77
r = 100 
omega = (frekvens*2*np.pi)**2
absq = Arms**2/Brms**2
model = sp(omega,absq)
a1 , b1 = model.slope ,model.intercept 
au,bu = model.stderr, model.intercept_stderr
print(au,bu) 
L = np.sqrt(r**2*a1)
print(L)
plt.plot(omega,omega*a1+b1)
plt.plot(omega,absq,'o')
plt.show()

res = sp(likestromsnitt,frekvens)
a = res.slope
b = res.intercept 

x = np.linspace(400,512_000,500)

plt.plot(frekvens,likestromsnitt)
plt.xscale('log')
plt.xlabel('Frekvens (hz)')
plt.ylabel('P_a')
#plt.plot(x,a*x)

plt.show()