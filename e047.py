from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=4, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()
result = 0

######## 

from Primes import factors2, is_prime

i = 0
count = n
while not result:
    i += 1
    if not is_prime(i):
        if len(set(factors2(i))) == n:
            count -= 1
        else:
            count = n
    else:
        count = n
    if not count:
        result = i - n 
    if args.verbose:
        print i, count
    
    


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

