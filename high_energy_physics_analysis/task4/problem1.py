import random
import math

def func_x4(x):
    return x**4

def MC_integrate_1D_w_error(func, n, x, y):
    MC_probe_vol = (x[1] - x[0]) * (y[1] - y[0])
    
    # probe with random hits
    hits = 0
    for i in range(0, int(n)):
        xr = random.uniform(x[0], x[1])
        yr = random.uniform(y[0], y[1])
        if yr <= func(xr):
            hits += 1
    
    # Since probes (shots) are independent and Bernoulli-distributed, the
    # whole ensemble is Binomial, thus the confidence interval for p:
    # https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    # and slightly inflated error for p (z=1) can be expressed as
    V_sigma = MC_probe_vol * (1 + 2 * (hits - hits**2 / float(n) + 0.25)**0.5 ) \
        / 2 / (float(n) + 1)
    V_result = (MC_probe_vol * (hits / float(n)))
    
    return V_result, V_sigma

if __name__ == '__main__':
    res, err = MC_integrate_1D_w_error(func_x4, n=1E6, x=[-3, 3], y=[0, 81])
    
    print("MC integral of x**4 = {:.2f} +- {:.2f}".format(res, err))
    real_val = 2 * 3**5 / 5
    print("Actual error: {:.2f}".format(res - real_val))
