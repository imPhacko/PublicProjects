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

def promenence_scanner(ms, peak, dm_step_size):
    scan_min = 0
    i = 0
    while i < peak[1]:
        if (peak[0] - ms[i]) <= 0.5 * dm_step_size:
            scan_min = i
            i = peak[1]
        i += 1
    
    n = len(ms)
    scan_max = 0
    i = peak[1]
    while i < n:
        if (ms[i] - peak[1]) >= 0.5 * dm_step_size:
            scan_max = i
            i = n
        i += 1
    
    i0 = scan_min
    m_last = ms[i0]
    
    #best_ii = peak[0]
    #best_ie = peak[1]
    best_n = peak[2]
    i = scan_min
    while i < scan_max:
        if (ms[i] - m_last) < dm_step_size:
            i += 1
            continue
        entries = i - i0
        
        if entries > best_n:
            #best_ii = i0
            #best_ie = i
            best_n = entries
        i0 += 1
        m_last = ms[i0]
        i -= 1 # to control large jumps in case they happen
    
    return best_n

def silly_bump_hunter(ms, dm_step_size=2):
    m_sorted = sorted(ms)
    n = len(ms)
    
    i0 = 0
    m_last = m_sorted[0]
    entries_last = 0
    candidates = []
    for i in range(0, n):
        #print(i)
        if (m_sorted[i] - m_last) < dm_step_size:
            continue
        entries = i - i0
        
        if entries > 2 * entries_last:
            candidates.append([i0, i, entries])
        entries_last = entries
        i0 = int(i0 + entries / 2)
        m_last = m_sorted[i0]
    
    by_prominence_cands = sorted(candidates, key=lambda x: -x[2])
    
    return promenence_scanner(m_sorted, by_prominence_cands[0], dm_step_size)

def main(filename):
    ms = []
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
            p = p1 + p2 + p3 + p4
            m = p.mass()
            ms.append(m)
    
    n_bump = silly_bump_hunter(ms)
    bkg = len(ms) - n_bump
    print('Estimated rates: n(signal) = {}, n(bkg) = {}'.format(n_bump, bkg))
    
    plt.hist(ms, 40)    # too few events, binning by hand
    plt.xlabel(r'$m_{4\ell}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3c.pdf')
    plt.savefig('output/problem3c.png')
    plt.close()
    
    plt.hist(ms, 400)    # too few events, binning by hand
    plt.xlabel(r'$m_{4\ell}$')
    plt.ylabel('n events')
    plt.savefig('output/problem3d.pdf')
    plt.savefig('output/problem3d.png')
    plt.close()

if __name__ == '__main__':
    main('data/pp_4l_all.csv')
