import csv
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import problem3a as p3a

def pass_4l_selection(p1, p2, p3, p4):
    p = p1 + p2 + p3 + p4
    m = p.mass()
    if m < 150 and m > 100:
        return True
    return False

def get_mZ12(p1, p2, p3, p4):
    """
    Output: mZ1, mZ2,
    in case of 4e/4mu, one particle pair is chosen such that it is closest to mZ
    """
    ps = sorted([p1, p2, p3, p4], key=lambda x: x.pdg)
    ids = [ps[0].pdg, ps[1].pdg, ps[2].pdg, ps[3].pdg]
    
    if ids == [-13, -13, 13, 13]:
        mZ1a = (p1 + p3).mass()
        mZ1b = (p1 + p4).mass()
        mZ2a = (p2 + p3).mass()
        mZ2b = (p2 + p4).mass()
        
        d1a = abs(91.19 - mZ1a)
        d1b = abs(91.19 - mZ1b)
        d2a = abs(91.19 - mZ2a)
        d2b = abs(91.19 - mZ2b)
        
        closest = sorted([d1a, d1b, d2a, d2b])[0]
        if d1a == closest or d2b == closest:
            if mZ1a < mZ2b:
                return mZ2b, mZ1a
            return mZ1a, mZ2b
        
        if d1b == closest or d2a == closest:
            if mZ1b < mZ2a:
                return mZ2a, mZ1b
            return mZ1b, mZ2a
    
    if ids == [-11, -11, 11, 11]:
        mZ1a = (p1 + p3).mass()
        mZ1b = (p1 + p4).mass()
        mZ2a = (p2 + p3).mass()
        mZ2b = (p2 + p4).mass()
        
        d1a = abs(91.19 - mZ1a)
        d1b = abs(91.19 - mZ1b)
        d2a = abs(91.19 - mZ2a)
        d2b = abs(91.19 - mZ2b)
        
        closest = min([d1a, d1b, d2a, d2b])
        if d1a == closest or d2b == closest:
            if mZ1a < mZ2b:
                return mZ2b, mZ1a
            return mZ1a, mZ2b
        
        if d1b == closest or d2a == closest:
            if mZ1b < mZ2a:
                return mZ2a, mZ1b
            return mZ1b, mZ2a
    
    if ids == [-13, -11, 11, 13]:
        mZ1 = (p1 + p4).mass()
        mZ2 = (p2 + p3).mass()
        
        if mZ1 < mZ2:
            return mZ2, mZ1
        return mZ1, mZ2
    
    return -1, -1

def get_pTs4(p1, p2, p3, p4):
    """
    Sort pTs and return pT1 > pT2 > pT3 > pT4
    """
    pTs = [p1.pT(), p2.pT(), p3.pT(), p4.pT()]
    pTs_sort = sorted(pTs)
    
    return pTs_sort[3], pTs_sort[2], pTs_sort[1], pTs_sort[0]

def get_etas4(p1, p2, p3, p4):
    """
    Output: eta1, eta2, eta3, eta4,
    where particles are pT sorted.
    """
    ps = sorted([p1, p2, p3, p4], key=lambda x: -x.pT())
    
    return ps[0].eta(), ps[1].eta(), ps[2].eta(), ps[3].eta()

def plot_mZ1_mZ2(mZ1s, mZ2s):
    plt.hist(mZ1s, 40, fc=(1, 0, 0, 0.75))  # too few events, binning by hand
    plt.hist(mZ2s, 40, fc=(0, 1, 0, 0.75))
    plt.xlabel(r'$m_{\ell\bar{\ell}}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3b-1.pdf')
    plt.savefig('output/problem3b-1.png')
    plt.close()

def plot_pTs(pT1s, pT2s, pT3s, pT4s):
    plt.hist(pT1s, 25, fc=(0, 0, 0, 0.75))  # too few events, binning by hand
    plt.hist(pT2s, 25, fc=(1, 0, 0, 0.75))
    plt.hist(pT3s, 25, fc=(0, 1, 0, 0.75))
    plt.hist(pT4s, 25, fc=(0, 0, 1, 0.75))
    plt.xlabel(r'$p_{\rm T}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3b-2.pdf')
    plt.savefig('output/problem3b-2.png')
    plt.close()

def plot_etas(eta1s, eta2s, eta3s, eta4s):
    # too few events, binning by hand
    plt.hist(eta1s, 13, fc=(0, 0, 0, 0.5))
    plt.hist(eta2s, 13, fc=(1, 0, 0, 0.5))
    plt.xlabel(r'$\eta_{1/2}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3b-3-12.pdf')
    plt.savefig('output/problem3b-3-12.png')
    plt.close()
    
    plt.hist(eta3s, 13, fc=(0, 1, 0, 0.5))
    plt.hist(eta4s, 13, fc=(0, 0, 1, 0.5))
    plt.xlabel(r'$\eta_{3/4}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3b-3-34.pdf')
    plt.savefig('output/problem3b-3-34.png')
    plt.close()

def main(filename):
    mZ1s = []
    mZ2s = []
    pT1s = []
    pT2s = []
    pT3s = []
    pT4s = []
    eta1s = []
    eta2s = []
    eta3s = []
    eta4s = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for event in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            p1 = p3a.particle([float(x) for x in event[0:5]])
            p2 = p3a.particle([float(x) for x in event[5:10]])
            p3 = p3a.particle([float(x) for x in event[10:15]])
            p4 = p3a.particle([float(x) for x in event[15:20]])
            if not pass_4l_selection(p1, p2, p3, p4):
                continue
            mZ1, mZ2 = get_mZ12(p1, p2, p3, p4)
            pT1, pT2, pT3, pT4 = get_pTs4(p1, p2, p3, p4)
            eta1, eta2, eta3, eta4 = get_etas4(p1, p2, p3, p4)
            mZ1s.append(mZ1)
            mZ2s.append(mZ2)
            pT1s.append(pT1)
            pT2s.append(pT2)
            pT3s.append(pT3)
            pT4s.append(pT4)
            eta1s.append(eta1)
            eta2s.append(eta2)
            eta3s.append(eta3)
            eta4s.append(eta4)
    
    plot_mZ1_mZ2(mZ1s, mZ2s)
    plot_pTs(pT1s, pT2s, pT3s, pT4s)
    plot_etas(eta1s, eta2s, eta3s, eta4s)

if __name__ == '__main__':
    main('data/pp_4l_all.csv')
