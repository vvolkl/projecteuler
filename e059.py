

import numpy as np

def solve(verbose=True, n=100): 
    t = np.loadtxt('e059_cipher.txt', delimiter=',', dtype=int)
    # according to problem, key is only 3 chars long
    tsep = []
    for i in range(3):
        tsep.append(t[i::3])
    # calculate frequencies
    b = map(np.bincount, tsep)
    f = map(np.argsort, b)
    #most frequent character is probably space (32)
    key = [np.bitwise_xor(ef[-1],32) for ef in f]
    # decode
    m = [map(chr, np.bitwise_xor(x[0], x[1])) for x in zip(tsep, key)]
    tn = []
    for e in range(len(m[0])-1):
        for n in m:
            tn.append(n[e])
    #somehow 
    tn.append('.')
    result = sum(map(ord,tn))
    print ''.join(tn)
    return result

