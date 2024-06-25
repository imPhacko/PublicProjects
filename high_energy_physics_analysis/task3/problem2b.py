import problem1a
import problem1c

if __name__ == '__main__':
    distr_vals_Y = problem1a.generate_averages_uniform(0, 10, 50, 20000)
    distr_vals_A = problem1a.generate_averages_uniform(-2, 16, 50, 20000)
    pv_Y = problem1c.p_val(distr_vals_Y, 6)
    pv_A = problem1c.p_val(distr_vals_A, 6)
    
    # A quick and dirty CL_S calculation, assumptions about distributions
    # were implied (like the mean of A is on the right WRT observed)
    print('CL_S of obs = 6: {:.5f}'.format(pv_Y / (1 - pv_A)))
