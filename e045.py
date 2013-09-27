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

from Primes import is_pent, is_hex



result = 0
test = [1, 6, 15, 28, 45]
testp =[1, 5, 12, 22, 35]
if args.verbose:
    print "check for known numbers:"
    print test,map(is_hex,test)
    print testp, map(is_pent,test)
def triangle(num):
    return num*(num + 1) / 2
i = 0
while not result:
    i += 1
    num = triangle(i)
    if is_pent(num) and is_hex(num):
        if args.verbose:
            print "found one: ", num
        #we're looking for the next bigger one
        if num > triangle(285):
            result = num

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

