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

import decimal as dec
prec = 3000 
dec.getcontext().prec = prec
result = 0
cyc = 0
for num in np.arange(2,1001):
    d = dec.Decimal(1) / dec.Decimal(num)
    a = str(d)[2:]
    for j in np.arange(1,prec//2-2):
        if len(a)>prec - 3:
            l = [a[i:i+j] for i in range(0, len(a)-j-1, j)]
            if l.count(l[0]) == len(l):
                if args.verbose:
                    print num,l[0],j
                if cyc < j:
                    result = num
                    cyc = j
                break
        


if args.verbose:
    print 'cycle length:', cyc
print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

