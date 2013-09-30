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
result = 1

######## 

from Primes import is_prime, sieve

for num in xrange(2,1000000):
    if not is_prime(num) and num % 2:
	result = 0
        for e in sieve(num):
            for f in xrange(int(np.ceil(np.sqrt((num-e)/2))+1)):
                if args.verbose:
                    print num, e, f, result
                result += num == e + 2 * f**2 
    if not result:
        result = num
        break
                      
        


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

