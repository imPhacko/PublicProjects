import random
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import os

def is_inside_shape(x):
    return (x[0]**4 + 4 * x[1]**2 + 6 * x[2]**2 + 8 * x[3]**2 <= 40)

def MC_hyperbox_hits(inside_func, nhits, bound_min, bound_max):
    sz = len(bound_min)
    hit_vec = [[None] * sz] * int(nhits)
    # probe with random hits
    hits = 0
    while hits < nhits:
        x = [None] * sz
        for j in range(0, sz):
            xr = random.uniform(bound_min[j], bound_max[j])
            x[j] = xr
        if inside_func(x):
            hit_vec[hits] = x
            hits += 1
    
    return hit_vec

def fill_plot_x1x2(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[2]**2 + x[3]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[0] for x in v[:sz_frc]]
    Ys = [x[1] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_2$')
    if put_title:
        axis.set_title(r'$(x_3, x_4) \approx (0, 0)$')

def fill_plot_x1x3(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[1]**2 + x[3]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[0] for x in v[:sz_frc]]
    Ys = [x[2] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_3$')
    if put_title:
        axis.set_title(r'$(x_2, x_4) \approx (0, 0)$')

def fill_plot_x1x4(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[1]**2 + x[2]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[0] for x in v[:sz_frc]]
    Ys = [x[3] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_4$')
    if put_title:
        axis.set_title(r'$(x_2, x_3) \approx (0, 0)$')

def fill_plot_x2x3(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[0]**2 + x[3]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[1] for x in v[:sz_frc]]
    Ys = [x[2] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_2$')
    axis.set_ylabel(r'$x_3$')
    if put_title:
        axis.set_title(r'$(x_1, x_4) \approx (0, 0)$')

def fill_plot_x2x4(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[0]**2 + x[2]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[1] for x in v[:sz_frc]]
    Ys = [x[3] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_2$')
    axis.set_ylabel(r'$x_4$')
    if put_title:
        axis.set_title(r'$(x_1, x_3) \approx (0, 0)$')

def fill_plot_x3x4(fig, axis, vec, fraction, put_title=True):
    v = sorted(vec, key=lambda x: x[0]**2 + x[1]**2)
    sz = len(v)
    sz_frc = int(sz * fraction)
    
    Xs = [x[2] for x in v[:sz_frc]]
    Ys = [x[3] for x in v[:sz_frc]]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_3$')
    axis.set_ylabel(r'$x_4$')
    if put_title:
        axis.set_title(r'$(x_1, x_2) \approx (0, 0)$')
    
def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def bonus_plots(vec):
    fig, axs = plt.subplots(2, 3)
    #fig.tight_layout()
    ax = axs[0, 0]
    fill_plot_x1x2(fig, ax, vec, 1, False)
    ax = axs[0, 1]
    fill_plot_x1x3(fig, ax, vec, 1, False)
    ax = axs[0, 2]
    fill_plot_x1x4(fig, ax, vec, 1, False)
    
    ax = axs[1, 0]
    fill_plot_x2x3(fig, ax, vec, 1, False)
    ax = axs[1, 1]
    fill_plot_x2x4(fig, ax, vec, 1, False)
    ax = axs[1, 2]
    fill_plot_x3x4(fig, ax, vec, 1, False)
    
    fig.subplots_adjust(left=0.08, right=0.97, hspace=0.5, wspace=0.5)
    plt.savefig('output/problem2c-1-bonus.pdf')
    plt.savefig('output/problem2c-1-bonus.png')

def main(nhits):
    bound_max = [40**0.25, 10**0.5, 20**0.5 / 3**0.5, 5**0.5]
    bound_min = [-40**0.25, -10**0.5, -20**0.5 / 3**0.5, -5**0.5]
    vec = MC_hyperbox_hits(is_inside_shape, nhits, bound_min, bound_max)
    #random.shuffle(vec) # not really needed, depends how it is used
    
    fig, axs = plt.subplots(2, 3)
    #fig.tight_layout()
    ax = axs[0, 0]
    fill_plot_x1x2(fig, ax, vec, 0.1)
    ax = axs[0, 1]
    fill_plot_x1x3(fig, ax, vec, 0.1)
    ax = axs[0, 2]
    fill_plot_x1x4(fig, ax, vec, 0.1)
    
    ax = axs[1, 0]
    fill_plot_x2x3(fig, ax, vec, 0.1)
    ax = axs[1, 1]
    fill_plot_x2x4(fig, ax, vec, 0.1)
    ax = axs[1, 2]
    fill_plot_x3x4(fig, ax, vec, 0.1)
    
    mkdir('output')
    fig.subplots_adjust(left=0.08, right=0.97, hspace=0.5, wspace=0.5)
    plt.savefig('output/problem2c-1.pdf')
    plt.savefig('output/problem2c-1.png')
    
    bonus_plots(vec)

if __name__ == '__main__':
    main(1E6)
