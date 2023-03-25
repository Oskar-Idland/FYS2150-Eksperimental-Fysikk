import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.stats import linregress
import os
filepath = os.path.dirname(__file__)
data_path = filepath.split("\script")[0] + "\Data"
fig_path = filepath.split("\script")[0] + "\\fig"


def get_data(filename: str):
    lists = []
    with open(os.path.join(data_path, filename), 'r') as f:
        data = csv.reader(f)
        for row in data:  # Finds the number of columns in the data
            n = len(row)
            break

        for i in range(n):  # Creates n empty lists to store the data
            exec(f'list{i} = []')
            lists.append(eval(f'list{i}'))

        for row in data:  # Appends the data to the lists
            try:
                for i in range(n):
                    lists[i].append(float(row[i]))
            except IndexError:
                pass

    for i in range(n):  # Converts the lists to numpy arrays
        lists[i] = np.array(lists[i])

    return lists


def plot(x, y, label='', xlabel='', ylabel='', makefig=False, title='', log=False, scatter=False):

    if makefig:
        # Sets the figure size to A5 dimensions
        plt.figure(figsize=(5.827, 8.268))
        plt.title(title, fontsize=18)
        plt.xlabel(xlabel, fontsize=18)
        plt.ylabel(ylabel, fontsize=18, rotation='horizontal')
        plt.yscale('log'*log or 'linear')

    if scatter:
        plt.scatter(x, y, label=label, c='red')
    else:
        plt.plot(x, y, label=label)
        plt.legend(fontsize=18)

# 2.4


def O_2_4():
    ω, Va, Vb, θ = get_data('data2.2.csv')
    ω_sr = ω**2
    Vab_sr = (Va/Vb)**2
    model = linregress(ω_sr, Vab_sr)
    m, c = model.slope, model.intercept
    '''
    m = L^2/R^2
    L = √(m*R^2)
    '''
    R = 100  # Ω
    L = np.sqrt(m*R**2)
    print(
        f'L = {L:.2g} H, with a standard deviation of {1/(np.sqrt(2))*model.stderr:.2g}')

    plot(ω_sr, Vab_sr, 'Plot av innsamlet data', r'$ω^2$',
         r'$\left( \frac{V_a}{V_b} \right)^2$', makefig=True, title='Oppgave 2.4', scatter=True)

    plot(ω_sr, m*ω_sr + c, 'Plot av tilpasset linje')
    plt.savefig(os.path.join(fig_path, '2.4.pdf'))
    plt.show()


# 2.6
def O_2_6():
    # TODO: Dette er fullstending feil, må fikses. Se hvordan regne P_a
    ω = np.array([400,800, 4_000, 8_000, 16_000, 
                  32_000, 64_000,128_000,256_000,400_000])

    I_snitt = np.array([10.65,11.24,10.57, 11.16, 11.09,
                        10.8,8.82,6.495,2.31,207*1e-3])

    
    plot(np.log10(ω), I_snitt, r'$I_{snitt}$', r'$\log_{10}(ω)$',
         r'$I_{avg}$', makefig=True, title='Oppgave 2.6')
    
    plt.show()


# 3.3
def O_3_3():
    ω, Va, Vb = get_data('data3.csv')

    def plot_Va():
        plot(ω, Va, r'Va(ω)', r'$ω$', r'$V_a$',
             makefig=True, title='Oppgave 3.3: Lineær')
        plt.savefig(os.path.join(fig_path, '3.3 Va lin.pdf'))

        plot(np.log10(ω), Va, r'Va(ω)', r'$ω$', r'$V_a$', makefig=True,
             title='Oppgave 3.3: Logaritmisk')
        plt.savefig(os.path.join(fig_path, '3.3 Va log.pdf'))

    def plot_Vb():
        plot(ω, Vb, r'Vb(ω)', r'$ω$', r'$V_b$',
             makefig=True, title='Oppgave 3.3: Lineær')
        plt.savefig(os.path.join(fig_path, '3.3 Vb lin.pdf'))

        plot(np.log10(ω), Vb, r'Vb(ω)', r'$ω$', r'$V_b$', makefig=True,
             title='Oppgave 3.3: Logaritmisk')
        plt.savefig(os.path.join(fig_path, '3.3 Vb log.pdf'))

    # plot_Va()
    # plot_Vb()
    plot(Va, Vb, r'$V_a/V_b$', r'$Va$', r'$Vb$', makefig=True)
    plt.show()


def O_3_5():
    '''
    | Vu |          1
    |----| = ----------------- 
    | Vi |    √(1 + (ωRC)^2)

    Vi bruker dette forholdet for å finne C

            √(V_i^2 - V_u^2)
    C   =   ----------------
               V_u ⋅ R ⋅ ω
    '''
    ω, V_i, V_u = get_data('data3.csv')
    R = 10  # Ω
    C = np.sqrt((V_i**2 - V_u**2))/(V_u * R * ω)
    # plot(np.log10(ω), C, r'C(ω)', r'$ω$', r'$C$', makefig=True,
    #      title='Oppgave 3.5 Logaritmisk')
    # plt.savefig(os.path.join(fig_path, '3.5 log.pdf'))

    # plot(ω, C, r'C(ω)', r'$ω$', r'$C$', makefig=True, title='Oppgave 3.5: Lineær')
    # plt.savefig(os.path.join(fig_path, '3.5 lin.pdf'))
    # plt.show()



if __name__ == '__main__':
    # O_2_4()
    # O_2_6()
    # O_3_3() 
    # O_3_5()
    ...
