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
result = 0

for num in xrange(n):
    if str(num) == str(num)[::-1]:
        if args.verbose:
            print 'found palindrome in base 10: ', num
        s = str(bin(num))[2:]
        if s == s[::-1]:
            if args.verbose:
                print '\t and in base 2: ', s
            result = result + num




print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

