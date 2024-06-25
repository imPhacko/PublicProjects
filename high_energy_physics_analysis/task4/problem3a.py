import csv
import math
import matplotlib.pyplot as plt

class particle:
    pdg = 0
    E = 0
    px = 0
    py = 0
    pz = 0
    def __init__(self, four_vec):
        self.pdg = four_vec[0]
        self.E = four_vec[1]
        self.px = four_vec[2]
        self.py = four_vec[3]
        self.pz = four_vec[4]
    
    def print_components(self):
        print('({}, {}, {}, {}, {})'.format(self.pdg, self.E, self.px, self.py, self.pz))
    
    def __add__(self, p2):
        E = self.E + p2.E
        px = self.px + p2.px
        py = self.py + p2.py
        pz = self.pz + p2.pz
        return particle([0, E, px, py, pz])
    
    def mass(self):
        return (self.E**2 - self.px**2 - self.py**2 - self.pz**2)**0.5
    
    def pT(self):
        return (self.px**2 + self.py**2)**0.5
    
    def p(self):
        return (self.px**2 + self.py**2 + self.pz**2)**0.5
    
    def eta(self):
        denom = (self.p() - self.pz)
        nom = (self.p() + self.pz)
        if nom == 0:
            return -9E99
        if denom <= 0:
            return 9E99
        return 0.5 * math.log(nom / denom)

def better_than_dumb_nbins(array):
    """a crude nbin estimator"""
    a_min = min(array)
    a_max = max(array)
    n = len(array)
    
    x_sum = 0
    x2_sum = 0
    for x in array:
        x_sum = x + x_sum
        x2_sum = x**2 + x2_sum
    sd = math.sqrt(x2_sum / float(n) - (x_sum / float(n))**2)
    
    range_in_sd = (a_max - a_min) / sd
    n_sd = 0.34 * n
    # aim for 3% variation in sd block ~ sqrt(1100) / 1100
    n_targeti = n_sd / 1100.
    
    return int(n_targeti * range_in_sd)

def main(filename):
    m = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for event in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            p1 = particle([float(x) for x in event[0:5]])
            p2 = particle([float(x) for x in event[5:10]])
            p3 = particle([float(x) for x in event[10:15]])
            p4 = particle([float(x) for x in event[15:20]])
            p = p1 + p2 + p3 + p4
            m.append(p.mass())
    
    n_bins = better_than_dumb_nbins(m)
    
    plt.hist(m, n_bins, range=[50, 500])
    plt.xlabel('mass')
    plt.ylabel('events')
    plt.savefig('output/problem3a.pdf')
    plt.savefig('output/problem3a.png')

if __name__ == '__main__':
    main('data/pp_4l_all.csv')
