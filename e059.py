from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=100, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()
result = 0

######## 

t = np.loadtxt('cipher1.txt', delimiter=',', dtype=int)
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


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

