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

from itertools import chain
def factors2(n): 
    result = []
    # test 2 and all of the odd numbers
    # xrange instead of range avoids constructing the list
    for i in chain([2],xrange(3,n+1,2)):
        s = 0
        while n%i == 0:  #a good place for mod
            n /= i
            s += 1
        result.extend([i]*s) #avoid another for loop
        if n==1:
            return result


#ideas for improvement: check before adding number to
# save disk space
terms = []
i = 0
for a in np.arange(2,n+1):
    for b in np.arange(2,n+1):
        if args.verbose:
            print i,a,b
        terms.append(sorted(factors2(a)*b))
        i = i + 1

#terms = terms[np.nonzero(terms)] 
terms = np.array(terms)
result = np.alen( np.unique( terms) )

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

