import numpy as np 
import matplotlib.pyplot as plt
import os
filepath = os.path.dirname(__file__)

# Oppgave 1
    # a)
    
V = np.array([-5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 
               0.2, 0.4, 0.6, 0.8])
I = np.array([-25.33, -23.11, -20.91, -18.58, -16.35, -13.52, -11.14, -8.57, -5.88, -3.7, 0, 
                1.61,  12.86,  23.55, 129.3])


plt.scatter(V,I, color='blue', label='No light')

    # b)
    
V = np.array([-5, -4.5, -4, -3.5, -2.5, -2, -1.5, -1, -.5, 
               0, 0.2, 0.4, 0.6])
I = np.array([-24.77, -22.65, -20.55, -17.95, -15.41, -13.03, -10.19, -7.72, -4.78, -1.55,
              0.28, 7.33, 72.6])

plt.scatter(V,I, color='red', label=' With light')

plt.grid()
plt.legend()
plt.ylim(-30, 15)
plt.xlabel('Voltage [V]')
plt.ylabel('Current [mA]')
plt.savefig(os.path.join(filepath, 'Oppgave1.pdf'))
plt.show()