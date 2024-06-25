import problem1a
import problem1c
import math
from scipy.stats import norm


def get_quantiles(probabilities):
    quantiles = []
    for p in probabilities:
        # sqrt(100/12/50) ~= 0.408248290463863
        quantiles.append(norm.ppf(p) * 0.40824829 + 5)
        
    return quantiles

def aggregated_error(distr_vals):
    quantiles = get_quantiles([0.025, 0.16, 0.84, 0.975])
    
    pvs = []
    for q in quantiles:
        pvs.append(problem1c.p_val(distr_vals, q))
    
    # probability differences in 5 ranges
    r1 = 0.025 - pvs[0]
    r2 = 0.16 - 0.025 - pvs[1] + pvs[0]
    r3 = 0.84 - 0.16 - (1 - pvs[1] - pvs[2])
    r4 = 0.975 - 0.84 - (pvs[2] - pvs[3])
    r5 = 1 - 0.975 - pvs[3]
    
    return 0.2 * (r1**2 + r2**2 + r3**2 + r4**2 + r5**2)

if __name__ == '__main__':
    distr_vals = problem1a.generate_averages_uniform(0, 10, 50, 20000)
    err = aggregated_error(distr_vals)
    
    print('Aggregated error: {:.10f}'.format(err))
    print('Bonus: Aggregated error mod. sqrt(1/5 * err): {:.10f}'.format(math.sqrt(0.2 * err)))
