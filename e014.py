from __future__ import division
doc = """

Valentin Volkl """

import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000000, 
                   help='the main variable for our program')
args = parser.parse_args()
n=args.n
start = time.time()




def lenCollatz(b):
    global lengths
    l = 0
    a = b
    seq = []
    while a > 1 :
        if a & 0x01 :
            a = 3 * a + 1
            seq.append(a)
            l = l + 1
        elif a<b:
            lengths[b] = l + lengths[a >> 1] + 1 
            seq.append(a)
            return lengths[b], seq            
        else:
            a = a >> 1
            l = l + 1
            seq.append(a)
            
    lengths[a] = l
    return l, seq 

maxl = 0
maxj = 0
l = 0
j = 0
lengths = np.zeros(n)
i = np.arange(n)
for jlen in i:
 
    l, j = lenCollatz(jlen)
    print jlen,l , maxl
    if l > maxl:
        maxl = l
        maxj = j
        


print 'result:'
print  np.max(lengths), np.where(lengths == np.max(lengths))[0], maxl, maxj
print 'elapsed time:'
print time.time()-start
