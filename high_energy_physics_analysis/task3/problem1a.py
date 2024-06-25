import random
import math
import matplotlib.pyplot as plt
import os


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

def plot(in_array):
    n_bins = better_than_dumb_nbins(in_array)
    
    plt.hist(in_array, n_bins)
    plt.xlabel('y')
    plt.ylabel('n')
    plt.title('CLT in action')
    plt.savefig('output/problem1a.pdf')
    plt.savefig('output/problem1a.png')

def get_avg_X(f, f_arg_dict, n=100):
    a = []
    for i in range(n):
        a.append(f(**f_arg_dict))
    sum = 0
    for i in a:
        sum = sum + i
    
    return (sum / float(n))

def generate_averages_uniform(a, b, n_avg=100, n=100):
    f_params = {'a': a, 'b': b}
    
    rnd_avg_vals = []
    for i in range(n):
        x = get_avg_X(random.uniform, f_params, n_avg)
        rnd_avg_vals.append(x)
        
    return rnd_avg_vals

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

if __name__ == '__main__':
    vals = generate_averages_uniform(0, 10, 50, 20000)
    mkdir('output')
    plot(vals)
