import problem1a
import problem1c
"""
An overall close copycat of problem1c
"""

if __name__ == '__main__':
    distr_vals = problem1a.generate_averages_uniform(-2, 16, 50, 20000)
    pv = problem1c.p_val(distr_vals, 6)
    
    print('p-value of A_obs = 6: {:.5f}'.format(pv))
    print('Bonus: p-value of A_obs = 6: {:.2f}sigma'.format(problem1c.get_sigmas(pv)))
    problem1c.estim_p_val_accuracy(pv, 20000)
