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
result = 0

from itertools import permutations

def is_panmult(num):
    
    for x in range(999):
        x = int('9' + str(x))
        #if args.verbose:
         #   print "checking %i" % x
        for n in range(2,7 - len(str(x))):
            result = ""
            for i in range(1,n+1):
                result += str( x * i)
                #if args.verbose:
                #    print x,i, result
            if result == num:
                return True
    return False 
            
            
    


for e in permutations("987654321"):
    e = ''.join(e)
    if args.verbose:
        print "checking %s" % e
    if  is_panmult(e):
        result = e
        break




print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

