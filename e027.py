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

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps



#http://stackoverflow.com/questions/4545114
#
# sqrt(1000000000) = 31622
__primes = sieve(31622)
from bisect import bisect_left
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

result = 0
winner = [0,0]
tempresult = 0
primecand = np.array(sieve(1000))
primecand = np.concatenate((primecand,-primecand,[0]))
for b in primecand:
    for a in np.arange(-1000,1001):
        stillprime = True
        i = 0
        while stillprime:
            stillprime = is_prime(i*i + a * i + b)
            i = i + 1
        if i > result:
            result = i
            winner = a,b
        if args.verbose:
            print b,a,result,i



print 'result:'
print result, winner 
print 'elapsed time:'
print time.time()-start

