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

from Primes import is_prime

from itertools import permutations


#Note: Nine numbers cannot be done 
#(1+2+3+4+5+6+7+8+9=45 => always dividable by 3) 
#Note: Eight numbers cannot be done 
#(1+2+3+4+5+6+7+8=36 => always dividable by 3)

def greatest_pandigital():
    for n in range(1,8)[::-1]:
        s = ''.join( [ str(a) for a in range(1, n+1)[ ::-1 ] ] )
        if args.verbose:
            print 'checking %i pandigital numbers: ' % n, s
        for e in permutations( s ):
            e = ''.join( e )
            if args.verbose:
                print e
            if is_prime( int(e) ):
                return e        

result = greatest_pandigital()


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

