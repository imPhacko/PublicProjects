import random
import math
import matplotlib.pyplot as plt
import problem3a

def unboost_4momenta(pi, boost):
    beta2 = boost[0] * boost[0] + boost[1] * boost[1] + boost[2] * boost[2]
    gamma = 1 / math.sqrt(1 - beta2)
    
    # too small to boost
    if ((gamma - 1) < 0.001):
        return pi
    
    p0 = gamma * (pi[0] - boost[0] * pi[1] - boost[1] * pi[2] - boost[2] * pi[3])
    
    p1 = -gamma * boost[0] * pi[0] + \
        (1 + (gamma - 1) * boost[0] * boost[0] / beta2) * pi[1] + \
        (gamma - 1) * boost[0] / beta2 * (boost[1] * pi[2] + boost[2] * pi[3])
                        
    p2 = -gamma * boost[1] * pi[0] + \
        (1 + (gamma - 1) * boost[1] * boost[1] / beta2) * pi[2] + \
        (gamma - 1) * boost[1] / beta2 * (boost[0] * pi[1] + boost[2] * pi[3])
    
    p3 = -gamma * boost[2] * pi[0] + \
        (1 + (gamma - 1) * boost[2] * boost[2] / beta2) * pi[3] + \
        (gamma - 1) * boost[2] / beta2 * (boost[0] * pi[1] + boost[1] * pi[2])
        
    return [p0, p1, p2, p3]

def decay_4momentum(p):
    boost = [p[1] / p[0], p[2] / p[0], p[3] / p[0]]
    
    # unboost
    p_u = unboost_4momenta(p, boost)
    
    mass1 = random.uniform(a=0, b=p_u[0])
    mass2 = random.uniform(a=0, b=(p_u[0] - mass1))
    theta = random.uniform(a=0, b=math.pi)
    phi = random.uniform(a=0, b=2*math.pi)
    
    # for the back-to-back decay:
    # sqrt(m_1^2 + p^2) + sqrt(m_2^2 + p^2) = E =>
    # p = +- 0.5 sqrt(E^2 - 2 * m_1^2 - 2 * m_2^2 + 1/E^2 * [m_1^2 - m_2^2]^2)
    pmag = 0.5 * math.sqrt(p_u[0]**2 - 2 * mass1**2 - 2 * mass2**2 +
                           1 / (p_u[0]**2) * (mass1**2 - mass2**2)**2)
    
    p1x = pmag * math.sin(theta) * math.cos(phi)
    p1y = pmag * math.sin(theta) * math.sin(phi)
    p1z = pmag * math.cos(theta)
    p1E = math.sqrt(mass1**2 + pmag**2)
    p2E = math.sqrt(mass2**2 + pmag**2)
    
    p1 = [p1E, p1x, p1y, p1z]
    p2 = [p2E, -p1x, -p1y, -p1z]
    
    # boost back to the original frame
    negboost = [-boost[0], -boost[1], -boost[2]]
    p1_b = unboost_4momenta(p1, negboost)
    p2_b = unboost_4momenta(p2, negboost)
    
    return [p1_b, p2_b]

def simple_H_decay():
    pZ12 = decay_4momentum([125., 0., 0., 0.])
    lpair1 = decay_4momentum(pZ12[0])
    lpair2 = decay_4momentum(pZ12[1])
    
    return lpair1 + lpair2

def energies_of_simple_H_decays(n=1):
    E1 = n * [None]
    E2 = n * [None]
    E3 = n * [None]
    E4 = n * [None]
    
    for i in range(n):
        ps = simple_H_decay()
        E1[i] = ps[0][0]
        E2[i] = ps[1][0]
        E3[i] = ps[2][0]
        E4[i] = ps[3][0]
    
    return [E1, E2, E3, E4]

def plot1(in_array):
    n_bins = problem3a.better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('E, GeV')
    plt.ylabel('Number of generated events')
    plt.title('Distribution of E1')
    plt.savefig('plots/problem3b-1.pdf')
    plt.savefig('plots/problem3b-1.png')
    plt.close()

def plot2(in_array):
    n_bins = problem3a.better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('E, GeV')
    plt.ylabel('Number of generated events')
    plt.title('Distribution of E2')
    plt.savefig('plots/problem3b-2.pdf')
    plt.savefig('plots/problem3b-2.png')
    plt.close()

def plot3(in_array):
    n_bins = problem3a.better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('E, GeV')
    plt.ylabel('Number of generated events')
    plt.title('Distribution of E3')
    plt.savefig('plots/problem3b-3.pdf')
    plt.savefig('plots/problem3b-3.png')
    plt.close()

def plot4(in_array):
    n_bins = problem3a.better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('E, GeV')
    plt.ylabel('Number of generated events')
    plt.title('Distribution of E4')
    plt.savefig('plots/problem3b-4.pdf')
    plt.savefig('plots/problem3b-4.png')
    plt.close()

def main():
    E = energies_of_simple_H_decays(20000)
    
    problem3a.mkdir('plots')
    plot1(E[0])
    plot2(E[1])
    plot3(E[2])
    plot4(E[3])
    
    
    return 0

if __name__ == '__main__':
    main()
