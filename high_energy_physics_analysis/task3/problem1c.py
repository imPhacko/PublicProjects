import problem1a


def p_val(distr_vals, obs_val):
    """
    Calculates the observed p-value.
    Inputs: distribution values of the same weight,
        the observed value.
    """
    
    distr_vals_sorted = sorted(distr_vals)
    sz = len(distr_vals_sorted)
    
    below = 0
    for v in distr_vals_sorted:
        if v > obs_val:
            continue
        below += 1
    
    p_v = 1 - below / sz
    if p_v > 0.5:
        p_v = 1 - p_v
    
    return p_v

def get_sigmas(p_val):
    from scipy.stats import norm
    
    return -norm.ppf(p_val)

def estim_p_val_accuracy(pv, entries):
    relat_acc = 1 / pv / entries
    print('Estimated uncertainty ("accuracy") is {:.2f}%.'.format(
        relat_acc * 100))

if __name__ == '__main__':
    distr_vals = problem1a.generate_averages_uniform(0, 10, 50, 20000)
    pv = p_val(distr_vals, 6)
    
    print('p-value of Y_obs = 6: {:.5f}'.format(pv))
    print('Bonus: p-value of Y_obs = 6: {:.2f}sigma'.format(get_sigmas(pv)))
    estim_p_val_accuracy(pv, 20000)
