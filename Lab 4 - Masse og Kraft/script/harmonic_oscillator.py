import numpy as np

tau = 0.2*np.array([2.10, 1.94, 1.99, 1.96, 2.02, 2.07, 2.06, 2.12, 2.03, 2.04])  # Period measurements with aluminium weight
tau2 = 0.2*np.array([2.04, 2.04, 2.03, 2.05, 2.11, 2.11, 1.97, 2.03, 1.88, 2.01])  # Period measurements with aluminium weight and extra weight
m = 2143.4

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


# Mean and standard deviation of the mean of the periods with the aluminium weight
print(f'σ τ_1: {mean(tau)}')
print(f'σ mean τ_1: {mean_std(tau)}')

# Mean and standard deviation of the mean of the periods with the aluminium weight and extra weight
print(f'σ τ_2: {mean(tau2)}')
print(f'σ mean τ_2: {mean_std(tau2)}')

print(f'Δm: {2*m*mean_std(tau)/mean(tau): .4g} [g]')