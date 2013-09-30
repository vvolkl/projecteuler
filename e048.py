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
result = []

######## 

from itertools import combinations_with_replacement, permutations
from Primes import is_prime

for e in combinations_with_replacement(range(10),4):
    f = [reduce(lambda rst, d: rst * 10 + d, seq) for seq in permutations(e) if seq[0] != 0]
    truth = np.array(map(is_prime,f))
    if sum( truth ) > 2:
        f = np.array(f)[truth]
        diff = [[f[j]-f[i] for i in range(j)] for j in range(len(f))]
        if args.verbose:
            print "found candidates: ", f, 
        if sum([g.count(3330) for g in diff]) > 1:
            result.append(np.unique(np.array([[[f[i],f[j]] for i in range(j) if f[j] - f[i] == 3330] for j in range(len(f))] ).flatten()))
            if args.verbose:
                print "found it: ", f
    if args.verbose:
        print e,f
    if len(result) > 2:
        break
    
    





print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

