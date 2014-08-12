from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
import primehelpers

import itertools
from Primes import *

parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1100, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()
result = 0

######## 

p = sieve(n**2)
try:
    checked = np.load('e060.temp.npy')
    print 'loaded check table!'
except:
    print 'generating checkTwoPrimeTable...'
        #print e
    checked = np.zeros((n+1,n+1))
    for i in range(n):
        for j in range(i,n):
            checked[i,j] = primehelpers.checkTwoPrimes(p[i], p[j]) > 0
    #print np.nonzero(checked)
#print 'generating combo-array...'
#combo = itertools.combinations(range(n), 4)
#dynCombo = np.array([e for e in combo]) 

nz1, nz2 = np.nonzero(checked)
for i in range(1,n):
    print i
    for j in range(i+1,n):
        v = np.intersect1d(nz2[np.argwhere(nz1==i)],nz2[np.argwhere(nz1==j)])
        #print v
        for k in v:
            w = np.intersect1d(nz2[np.argwhere(nz1==k)], v)
            #print '\t ',k, w
            for l in w:
                x = np.intersect1d(nz2[np.argwhere(nz1==l)], w)
                #print '\t->\t', l, x
                if np.any(x):
                    print 'found it!'
                    result = [i,j,k,l] + x
                    break
            if result:
                break
        if result:
            break
    if result:
        break

"""
            for l in w:
                x = np.intersect1d(nz2[np.argwhere(nz1==l)], w)
                #print '\t->\t', l, x
                if x:
                    print 'found it!'
                    result = [i,j,k,l]
                    break
"""
"""
for e in itertools.combinations(range(100),4):
    result = 1
    #print e
    for f in itertools.combinations(e,2):
        if  checked[f[0],f[1]] == 0:
            result = 0
            break 
    if result:
        break
"""


print 'indices of result:'
print result 
print 'result:'
print [p[r] for r in result]
print  'sum:'
 
print sum([p[r] for r in result])
print 'elapsed time:'
print time.time()-start

