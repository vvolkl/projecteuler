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

from Primes import is_prime, sieve

__primes = np.array(sieve(1000000))

def len_cons_primes(prim):
    c  = sieve(prim)
    r = []
    for i in range(len(c)):
        a = prim
        j = 0
        while a > 0:
            a -= c[j+i]
            j += 1
        if a == 0:
            r.append(j)
    return max(r)

resultlen = 0
for num in __primes[__primes > 100000]:
    t = len_cons_primes(num)
    if t > resultlen:
        resultlen = t
        result = num
    if args.verbose:
        print num, t, resultlen, result
        
        
    



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

