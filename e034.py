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

from math import factorial
result = 0
for num in xrange(3,4000000):
    s = str(num)
    if sum(map(factorial, map(int,s))) == num:
        if args.verbose:
            print "found it! %i" % num
        result = result + num



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

