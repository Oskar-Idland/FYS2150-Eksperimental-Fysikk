import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
a = 3.5
b = 5.0
x = np.arange(0,10,0.1)
y = a + b*x + (np.random.randn(len(x)))
plt.style.use("seaborn")
plt.plot(x,y,"*",label="data")

fit = stats.linregress(x,y)

m = fit.slope
c = fit.intercept

def least_squares_line(x, y, n):
    '''
    Bruker formelen for en generell linje og n data punkter x_i og y_i
    y = mx + c
    m = E/D
    c =  y_mean - m*x_mean
    
    Returnerer stigningstall m og konstant c
    '''
    D = sum(x**2) - 1/n * sum(x)**2
    E = sum(x*y) - 1/n * sum(x)*sum(y)
    x_mean = sum(x)/n
    y_mean = sum(y)/n
    m = E/D
    c = y_mean - m*x_mean
    return m, c

m_2, c_2 = least_squares_line(x,y,len(x))

plt.plot(x,m*x+c,label="linfit:{:.3f} x + {:.3f}".format(m,c), linewidth = 4)
plt.plot(x, m_2*x + c_2, label="linfit_2:{:.3f} x + {:.3f}".format(m_2,c_2), linestyle = ":", linewidth = 4)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#standardfeil i estimatene

dm = fit.stderr
dc = fit.intercept_stderr

#R2 sier not om goodness of fit. 0 er veldig dårlig, 1 er veldig bra.
R2 = fit.rvalue**2

print("SE(m) = {:.3f}".format(dm))
print("SE(c) = {:.3f}".format(dc))
print("R2 = {:.3f}".format(R2))