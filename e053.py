from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
from scipy import misc
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


def smart():
    result = 0
    m = 100
    doub = False
    set_doub=False
    for n in range(args.n+1):
        for r in range(min(m,n+1)):
            if misc.comb(n,r) < 1e6:
                if doub:
                    result += 2
                else:
                    result += 1
                
                if args.verbose:
                    print n,r,result, misc.comb(n,r)  
            else:
                m=r+1 
                set_doub=True
        if set_doub:
            doub=True

    return np.sum(range(n+2)) - result

def brute_force():
    result = 0
    for N in range(n+1):
        for r in range(N+1):
            if misc.comb(N,r)>1e6:
                result = result + 1
                if args.verbose:
                    print r,N,misc.comb(N,r)
    return result
        


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

