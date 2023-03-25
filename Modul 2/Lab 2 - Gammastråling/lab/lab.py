import numpy as np 
import matplotlib.pyplot as plt
import os 
filepath = os.path.dirname(__file__)
figpath = os.path.join(filepath, 'fig')
datapath = os.path.join(filepath, 'data')


# Oppgave 1.1
with open(os.path.join(datapath, 'gm_100pulser.csv'), 'r') as f:
    data = []
    for line in f.readlines():
        data.append(float(line.split(',')[1].strip()[1:-1]))
        
        
plt.hist(data, bins= len(set(data)), label = 'Empirisk verdier')
plt.xlabel('k')
plt.ylabel('N', rotation=0)
plt.title('Histogram for k-verdi over 100 pulser')
plt.savefig(os.path.join(figpath, 'histogram_1.1.pdf'))
# plt.show()

# Oppgave 1.2
N = 100
k_mean = np.mean(data) 
k_σ = np.std(data) 
print(f'k_mean = {k_mean}, k_σ = {k_σ}, √k_mean = {np.sqrt(k_mean)}')

# Oppgave 1.3
m = k_mean # Tilnærming ettersom m er ukjent
y_0 = N*np.exp(-m)
y_prev = y_0
y = [y_0]
for i in range(1,len(set(data)) + 1):
    y_current = m/i * y_prev
    y.append(y_current)
    y_prev = y_current
    
plt.plot(y, label='Teoretisk tilnærming', color = 'orange')
plt.legend()
plt.savefig(os.path.join(figpath, 'histogram_1.3.pdf'))
# plt.show()
plt.close()


# Oppgave 3.1&2

def load_txt(filename):
    with open(os.path.join(datapath, filename), 'r') as f:
        channel = []
        count = []
        f.readline()
        for line in f:
            channel.append(int(line.split()[0]))
            count.append(int(line.split()[1]))
    
    return np.array(channel), np.array(count)


noise_channel, noise_count  = load_txt('noise.txt')
cs_channel, cs_count        = load_txt('cs.txt')
co_channel, co_count        = load_txt('co.txt')
watch_channel, watch_count  = load_txt('watch.txt')

cs_count    -= noise_count # Fjerner støy
co_count    -= noise_count # Fjerner støy
watch_count -= noise_count # Fjerner støy

plt.plot(cs_channel, cs_count)
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title(r'$C_s$')
plt.xlim(25,225)
plt.savefig(os.path.join(figpath, 'cs.pdf'))
# plt.show()
plt.close()

plt.plot(co_channel, co_count)
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title(r'$C_o$')
plt.xlim(25,425)
plt.savefig(os.path.join(figpath, 'co.pdf'))
# plt.show()
plt.close()

plt.plot(watch_channel, watch_count)
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Watch')
plt.xlim(0, 400)
plt.savefig(os.path.join(figpath, 'watch.pdf'))
# plt.show()
plt.close()

cs_top_channel      = np.where(np.max(cs_count) == cs_count)[0][0]
co_top_channel_1    = np.where(np.max(co_count[300:370]) == co_count[300:370])[0][0]    + 300
co_top_channel_2    = np.where(np.max(co_count[370:]) == co_count[370:])[0][0]          + 370
watch_top_channel   = np.where(np.max(watch_count[150:]) == watch_count[150:])[0][0]    + 150

print(f'cs top channel    = {cs_top_channel}')
print(f'co top channel 1  = {co_top_channel_1}')
print(f'co top channel 2  = {co_top_channel_2}')
print(f'watch top channel = {watch_top_channel}')