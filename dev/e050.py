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
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()
result = []

######## 

from Primes import is_prime, sieve
import gmpy
__primes = np.array(sieve(1000000))

def len_cons_primes(prim):
    #c  = sieve(prim)
    #print prim
    c = __primes[__primes < prim/2 ]
    r = [0]
    
    for i in range(int(len(c)))[::-1]:
        a = prim
        j = i
        primsum = 0
        while primsum < prim and j < len(c): 
            #a -= c[j]
            
            primsum = np.sum(c[i:j])
            j = j + 1
            #print '\t',i,j,np.sum(c[i:j]),prim
        if primsum == prim:
            #if a < 1:
            #    if a == 0:
                r.append(j-i - 1)
            #    continue
    return max(r)


def check_primes_for_sums():
    resultlen = 0
    print 'n', n
    for num in __primes[(__primes < n) *(__primes > n/2)]:
        t = len_cons_primes(num)
        if t > resultlen:
            resultlen = t
            result = num
        if args.verbose:
            print num, t, resultlen, result
        
def check_sums_for_prime():    
    result = 0
    l = 0
    for (prim,i) in zip(__primes[:20],range(20)):
        s = 0
         
        j = i
        while s + __primes[j] < n:
            s += __primes[j]
            if is_prime(s):
                if j - i > l:
                    l = j - i
                    result = s
                if args.verbose:
                    print prim,result,s,l,j-i
            j = j + 1
    return result


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

