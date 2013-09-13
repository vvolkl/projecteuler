from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000, 
                   help='the main variable for our program')
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

result = 0
results = np.zeros(n)
        
for p in range(2,n + 1):
    #if args.verbose:
        #print 'checking p:',p
    for a in range(1,p+1):
        for b in range(1,p-a):
            c = p - a - b
            #if args.verbose:
             #   print 'checking sides ', a,b,c
            if a ** 2 + b ** 2 == c**2:
                if args.verbose:
                    print "\t found one: ", a, b, c, p
                results[ p ] += 1
                    

result = np.where(results == np.amax(results))[0]

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

