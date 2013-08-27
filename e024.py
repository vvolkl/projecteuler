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


from itertools import permutations

i = 0
for e in permutations(range(10)):
    i = i + 1
    if i == 1000000:
        result = e
        break
result = ''.join(map(str,result))



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

