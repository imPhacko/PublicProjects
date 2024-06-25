import random
import math
import matplotlib.pyplot as plt
import problem3a
import problem3b

def invariant_masses_of_simple_H_decays(n=1):
    M = n * [None]
    
    for i in range(n):
        ps = problem3b.simple_H_decay()
        E_sum = ps[0][0] + ps[1][0] + ps[2][0] + ps[3][0]
        px_sum = ps[0][1] + ps[1][1] + ps[2][1] + ps[3][1]
        py_sum = ps[0][2] + ps[1][2] + ps[2][2] + ps[3][2]
        pz_sum = ps[0][3] + ps[1][3] + ps[2][3] + ps[3][3]
        M[i] = math.sqrt(E_sum**2 - (px_sum + py_sum + pz_sum)**2)
    
    return M

def plot(in_array):
    n_bins = problem3a.better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('M, GeV')
    plt.ylabel('Number of generated events')
    plt.title('Distribution of M')
    plt.savefig('plots/problem3c.pdf')
    plt.savefig('plots/problem3c.png')
    plt.close()

def main():
    M = invariant_masses_of_simple_H_decays(20000)
    
    problem3a.mkdir('plots')
    
    plot(M)
    
    return 0

if __name__ == '__main__':
    main()
