import random
import math
import matplotlib.pyplot as plt
import os


def generate_normal_array(mu, sigma, n):
    array = int(n) * [None] # preallocate for performance
    for i in range(int(n)):
        array[i] = random.normalvariate(mu, sigma)
    
    return array

def better_than_dumb_nbins(array):
    """a crude nbin estimator"""
    a_min = min(array)
    a_max = max(array)
    n = len(array)
    
    x_sum = 0
    x2_sum = 0
    for x in array:
        x_sum = x + x_sum
        x2_sum = x**2 + x2_sum
    sd = math.sqrt(x2_sum / float(n) - (x_sum / float(n))**2)
    
    range_in_sd = (a_max - a_min) / sd
    n_sd = 0.34 * n
    # aim for 3% variation in sd block ~ sqrt(1100) / 1100
    n_targeti = n_sd / 1100.
    
    return int(n_targeti * range_in_sd)

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def plot(in_array):
    n_bins = better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('m, GeV')
    plt.ylabel('number of generated events')
    plt.title('Normal distribution of Higgs masses')
    plt.savefig('plots/problem3a.pdf')
    plt.savefig('plots/problem3a.png')

def main():
    a = generate_normal_array(125., 0.002, 2e+4)
    mkdir('plots')
    plot(a)
    
    return 0

if __name__ == '__main__':
    main()
