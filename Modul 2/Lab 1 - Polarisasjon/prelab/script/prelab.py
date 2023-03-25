import numpy as np 
import matplotlib.pyplot as plt
import os 
filepath = os.path.dirname(__file__)
datapath = os.path.join(filepath[:-len('script')], 'data')

for i, filename in enumerate(os.listdir(datapath)):
    data = np.loadtxt(os.path.join(datapath, filename))
    plt.subplot(3,1,i+1)
    plt.plot(data[:,0], data[:,1], label=f'{filename[:-4]}')
    plt.legend()
    
plt.show()