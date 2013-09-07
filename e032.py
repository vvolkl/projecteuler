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

results = []
for a in xrange(1,9999):
    if args.verbose:
        print a
    for b in xrange(1,min(a,100)):
        t = str(a)+str(b)
        if np.alen(np.unique(t)) == np.alen(t):
            prod  = a * b 
            t = t+str(prod)
            if '0' not in t and np.alen(np.unique(t)) == np.alen(t) == 9:
                if args.verbose:
                    print "found pandigital: %i * %i = %i" % (a,b,prod)
                results.append(prod)
       


result = np.sum(np.unique(results))


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

