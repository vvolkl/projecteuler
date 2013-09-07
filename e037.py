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

from Primes import is_prime, sieve

result = 0
pfound = 0
results = []
i = 8
while pfound < 11:
    if is_prime(i): # and ['4','6','8','0'] not in str(i):
        if args.verbose:
            print 'checking prime ', i
       
        s = str(i)
        relevance = 1
        for j in xrange(len(s)):
            num = s[j:]
            if args.verbose:
                print '\t truncating from left, now checking ', num
            if not is_prime(int(num)):
                relevance = 0
                break
            num = s[:j+1]
            if args.verbose:
                print '\t truncating from right, now checking ', num
            if not is_prime(int(num)):
                relevance = 0
                break
            #j = j + 1
        if relevance:
            if args.verbose:
                print 'found it: ', i
            results.append(i)
            pfound = pfound + 1
    i = i + 1 
            
            
        
        
        
            


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

