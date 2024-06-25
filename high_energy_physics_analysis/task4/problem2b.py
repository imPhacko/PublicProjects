import random

def is_inside_shape(x):
    return (x[0]**4 + 4 * x[1]**2 + 6 * x[2]**2 + 8 * x[3]**2 <= 40)

def MC_hyperbox_w_error(inside_func, n, bound_min, bound_max):
    MC_probe_vol = 1
    for i, j in zip(bound_max, bound_min):
        MC_probe_vol *= (i - j)
    
    sz = len(bound_min)
    # probe with random hits
    hits = 0
    for i in range(0, int(n)):
        x = [None] * sz
        for j in range(0, sz):
            xr = random.uniform(bound_min[j], bound_max[j])
            x[j] = xr
        if inside_func(x):
            hits += 1
    
    # Since probes (shots) are independent and Bernoulli-distributed, the
    # whole ensemble is Binomial, thus the confidence interval for p:
    # https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    # and slightly inflated error for p (z=1) can be expressed as
    V_sigma = MC_probe_vol * (1 + 2 * (hits - hits**2 / n + 0.25)**0.5 ) / 2 / (n + 1)
    V_result = (MC_probe_vol * (hits / float(n)))
    
    return V_result, V_sigma
    
def integrator_wrapper(n):
    bound_max = [40**0.25, 10**0.5, 20**0.5 / 3**0.5, 5**0.5]
    bound_min = [-40**0.25, -10**0.5, -20**0.5 / 3**0.5, -5**0.5]
    V, err = MC_hyperbox_w_error(is_inside_shape, n, bound_min, bound_max)
    
    return V, err

def dumb_algorithmic_n_finder(precision):
    """
    An algorithmic scan with some up/down extrapolation to get the number of
    needed MC integration points.
    Input: relative precision
    """
    V, err = 1, 1
    n = 1
    while err / V > precision:
        n *= 10
        Vm1, errm1 = V, err # keeping a previous iteration
        V, err = integrator_wrapper(n)
        if V == 0:
            V = 1E-10
        if err == 0:
            err = 1E10
        
    # extrapolating up and down, then taking an average.
    # somewhere in the ballpark of:
    n_x2 = (errm1 / Vm1 / precision)**2 * n / 10 + (err / V / precision)**2 * n
    n_est = int(n_x2 / 2)
    print("Estimated n to achieve ~1% precision: {}".format(n_est))
    
    V, err = integrator_wrapper(n_est)
    print("MC integral (@1%) of V = {:.2f} +- {:.2f}".format(V, err))

if __name__ == '__main__':
    V, est_err = integrator_wrapper(1E6)
    print("MC integral of V = {:.2f} +- {:.2f}".format(V, est_err))
    dumb_algorithmic_n_finder(0.01)
