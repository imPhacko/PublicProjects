import problem1a
import math


def eval_CI(distr_vals, CI_lvl):
    """
    A two-sided Confidence Interval of at least a chosen level.
    Level needs to be specified as a fraction.
    Inputs: distribution values of the same weight,
        required confidence level.
    """
    vals_sorted = sorted(distr_vals)
    sz = len(vals_sorted)
    
    CL_low = 0.5 - CI_lvl / 2.
    CL_up = 0.5 + CI_lvl / 2.
    # up to (<=) a quantile of
    quant_low = int(sz * CL_low)
    # at least (~= or >=) a quantile of
    quant_up = math.ceil(sz * CL_up)
    
    lower = vals_sorted[quant_low]
    upper = vals_sorted[quant_up]
    print('Confidence Interval at {} confidence level is ({:.2f}, {:.2f})'.\
        format(CI_lvl, lower, upper))
    
if __name__ == '__main__':
    distr_vals = problem1a.generate_averages_uniform(0, 10, 50, 20000)
    eval_CI(distr_vals, 0.68)
    eval_CI(distr_vals, 0.95)
    eval_CI(distr_vals, 0.99)
