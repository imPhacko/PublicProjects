## TASK LIST

### 1) Let there be a population $X_i \sim$ iid Uniform($a=0, b=10$), a combined rv is defined as $Y = \frac{1}{n}\sum_{i}^n X_i$. Suppose $n=50$:

a) Produce $m = 20000 y_i$ values that follow a rv $Y$ in order to graphically prove the Central Limit Theorem. Use a histogram to bin $y_i$ values.

b) Using a histogram (which is a pmf after the normalization: $\int \rightarrow 1$) ) from the previous step, estimate approximate confidence intervals (CIs) given the following confidence levels: 68, 95, and 99%. Produce two-sided CIs.

c) Assume the observed value is the following $x_{obs} = {6,6, ..., 6}$,  using the pmf from step 1a estimate the p-value for the given observation. Increase $m$ if deemed necessary in order to evaluate at 1% precision or better.

d) Analytically calculate the exact p-value for the observed $x_{obs}$. An exact joint pdf/cdf consisting of marginal uniform pdfs/cdfs is needed for such a calculation. Is the result different from 1c? Why? Also, see note at the end.

e) Use an actual $Normal(\mu = 5, \sigma^2 = \frac{100}{12 \cdot 50})$ in order to estimate an aggregated error using CLT via five bins. Let bins correspond to the following ranges:

$(-\infty, Q_{normal}(2.5\% )], (Q_{normal}(2.5\% ), Q_{normal}(16\% )], (Q_{norma}l(16\% ), Q_{normal}(84\% )], (Q_{normal}(84\% ), Q_{normal}(97.5\% )], (Q_{normal}(97.5\% ), +\infty)$.

Use corresponding five probability pairs in order to evaluate: $err = \frac{1}{5} \sum_{i=1}^{5} (P_{Normal} - P_{pmf})^2$ using $m = 20000$.


### 2) Let’s extend the previous problem with the second population $Z_i \sim$ idd Uniform($a=-2, b=16$), and the second combined rv $A = \frac{1}{n_2} \sum_{i}^{n_2}Z_i$. For simplicity, suppose $n = n_2 = 50$. Let 

$H_0: TS \sim Y$;

$H_A: TS \sim A$.

Given the same observation of ${6,6, ...,6}$, the $TS_{obs} = 6$, using pmfs with $m = m_2 = 50000$ find the following:

a) Calculate the p-value given the $H_A$ is true.

b) Calculate the $CL_S$ criterion, where the “signal” is $H_0$.

c) Is data leaning towards $H_0$ or $H_A$? Why?
