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

from Primes import sieve

div =  sieve(18)

def check43(num):
    num = str(num)
    res = 1
    for i in range(len(div)):
        res *=  int(num[i+1:i+4]) % div[i] == 0
    return res
        
if args.verbose:
    assert check43(1406357289)
     


from itertools import permutations

pan = ''.join([str(a) for a in range(10)])
result = 0
for e in permutations(pan):
    e = ''.join(e)
    if check43(e):
        if args.verbose:
            print "found it!: ", e
        result = result + int( e )
print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

