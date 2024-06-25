import random
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import os
import importlib  
p2c1 = importlib.import_module("problem2c-1")

def is_inside_shape_x1x2(x):
    return (x[0]**4 + 4 * x[1]**2 <= 40)

def is_inside_shape_x1x3(x):
    return (x[0]**4 + 6 * x[1]**2 <= 40)

def is_inside_shape_x1x4(x):
    return (x[0]**4 + 8 * x[1]**2 <= 40)

def is_inside_shape_x2x3(x):
    return (4 * x[0]**2 + 6 * x[1]**2 <= 40)

def is_inside_shape_x2x4(x):
    return (4 * x[0]**2 + 8 * x[1]**2 <= 40)

def is_inside_shape_x3x4(x):
    return (6 * x[0]**2 + 8 * x[1]**2 <= 40)

def fill_plot_x1x2(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_2$')
    axis.set_title(r'$(x_3, x_4) = (0, 0)$')

def fill_plot_x1x3(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_3$')
    axis.set_title(r'$(x_2, x_4) = (0, 0)$')

def fill_plot_x1x4(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_1$')
    axis.set_ylabel(r'$x_4$')
    axis.set_title(r'$(x_2, x_3) = (0, 0)$')

def fill_plot_x2x3(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_2$')
    axis.set_ylabel(r'$x_3$')
    axis.set_title(r'$(x_1, x_4) = (0, 0)$')

def fill_plot_x2x4(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_2$')
    axis.set_ylabel(r'$x_4$')
    axis.set_title(r'$(x_1, x_3) = (0, 0)$')

def fill_plot_x3x4(fig, axis, vec):
    Xs = [x[0] for x in vec]
    Ys = [x[1] for x in vec]
    h = axis.hist2d(Xs, Ys, bins=[40, 40], cmap='jet')
    fig.colorbar(h[3], ax=axis)
    axis.set_xlabel(r'$x_3$')
    axis.set_ylabel(r'$x_4$')
    axis.set_title(r'$(x_1, x_2) = (0, 0)$')

def main(nhits):
    fig, axs = plt.subplots(2, 3)
    
    bound_max = [40**0.25, 10**0.5]
    bound_min = [-40**0.25, -10**0.5]
    ax = axs[0, 0]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x1x2, nhits, bound_min, bound_max)
    fill_plot_x1x2(fig, ax, vec)
    
    bound_max = [40**0.25, 20**0.5 / 3**0.5]
    bound_min = [-40**0.25, -20**0.5 / 3**0.5]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x1x3, nhits, bound_min, bound_max)
    ax = axs[0, 1]
    fill_plot_x1x3(fig, ax, vec)
    
    bound_max = [40**0.25, 5**0.5]
    bound_min = [-40**0.25, -5**0.5]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x1x4, nhits, bound_min, bound_max)
    ax = axs[0, 2]
    fill_plot_x1x4(fig, ax, vec)
    
    
    bound_max = [10**0.5, 20**0.5 / 3**0.5]
    bound_min = [-10**0.5, -20**0.5 / 3**0.5]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x2x3, nhits, bound_min, bound_max)
    ax = axs[1, 0]
    fill_plot_x2x3(fig, ax, vec)
    
    bound_max = [10**0.5, 5**0.5]
    bound_min = [-10**0.5, -5**0.5]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x2x4, nhits, bound_min, bound_max)
    ax = axs[1, 1]
    fill_plot_x2x4(fig, ax, vec)
    
    bound_max = [20**0.5 / 3**0.5, 5**0.5]
    bound_min = [-20**0.5 / 3**0.5, -5**0.5]
    vec = p2c1.MC_hyperbox_hits(is_inside_shape_x3x4, nhits, bound_min, bound_max)
    ax = axs[1, 2]
    fill_plot_x3x4(fig, ax, vec)
    
    p2c1.mkdir('output')
    fig.subplots_adjust(left=0.08, right=0.97, hspace=0.5, wspace=0.5)
    plt.savefig('output/problem2c-2.pdf')
    plt.savefig('output/problem2c-2.png')

if __name__ == '__main__':
    main(1E5)
