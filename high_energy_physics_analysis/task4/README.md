Run one by one or simply `bash run_all.sh`


## TASK LIST


### 1) Using the numeric MC integration with $n = 106$ points evaluate the following:

$$
\int_{-3}^{3} x^4 \, dx
$$

Estimate numeric error.

### 2) Apply Monte Carlo methods to investigate $x_{1}^{4} + x_{2}^{2} + 6x_{3}^{2} + 8x_{4}^{2} = 40$.

a) Analytically derive the hypercube(-cuboid) boundaries that confine the shape.

b) MC integrate the volume of the given shape and estimate the numeric error. Use $n=10^6$. Estimate the $n$ that is sufficient to get to a 1% precision.

c) Draw all six 2D projected cross sections ($x_i$ vs. $x_j$) in $(x_k, x_l) = (0, 0)$ planes.

i. Increase $n$ so that there is a total of $m = 106$ “hits”. Use these (“hit”) points to draw 2D projections in the ±5% vicinity to $(0, 0)$ planes. An exact plane has a probability infinitesimally close to zero. Cross sections will be approximated be sets of 10% of $n = 10^6$ points, i.e., $10^5$ each.

ii. Use an analytic function zeroed at the corresponding plane (thus 6 variations). Recalculate the MC points in the planes and plot the “hitting” $m = 10^5$ points that correspond to areas under study. Plot six sets of $m = 10^5$. 


### 3) Events are four four-momenta preceded by the PDG IDs; the format: {PDG ID, E, px, py, pz}. One event (20 numbers) corresponds to a single line in the csv file.

Using the events available at https://cernbox.cern.ch/index.php/s/TX3fDAVFyn3vsBe/download produce the following plots (histograms):

a) $m_{4l}$ distribution.

b) Use the selection (cut) of $m_{4l} = (100; 150)$ to plot:

i. $m_{Z_1}, m_{Z_2}$, where $m_{Z_1} \> m_{Z_2}$.

ii. $p_{T_1}, p_{T_2}, p_{T_3}, p_{T_4}$, where $p_{T_1} \> p_{T_2} \>$ ...

iii. $\eta_{1}, \eta_{2}, \eta_{3}, \eta_{4}$, where particles are $p_T$ ordered. 

c) Estimate overall integrated rates (nr. of events per each) of the signal and the background processes using $m_{4l} = (100; 150)$.

d) Are events taken from the MC simulation or are they reconstructed from the detector data?

