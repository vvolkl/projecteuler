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




with open('e042words.txt') as f:
    words = f.read()

words = words.replace('"', '').split(',')
mlen = max( map(len, words) )
if args.verbose:
    print words[0:10], '...'
    print "longest word has %i letters" % mlen

maximum = 26 * mlen

triangles = [ n * ( n+1 ) / 2 for n in range(1, maximum) ]

if args.verbose:
    print "triangle hash list: ", triangles[0:10], "..."


result = sum( [ sum( [ord(d) - 64 for d in w ]) in triangles for w in words ] )
        
    
        



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

