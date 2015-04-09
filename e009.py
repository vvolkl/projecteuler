from __future__ import division
doc = """


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Valentin Volkl """

import argparse
import numpy as np
import re
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000, 
                   help='the main variable for our program')
args = parser.parse_args()
n=args.n

class MyException(Exception):
    #print a,b,c,d
    #print 'found it!'
    pass


#find all the pythagorean triplets below 1000:
summe = 0

for a in np.arange(1,n):
    for b in np.arange(1,n-a+1):
        b = b + a
        c = np.sqrt(a**2 + b**2)
        #summe = np.sum([a, b, c] )
        #print a,b,c, summe
        cc = np.ceil(c)
        
        if cc == c:
            if np.sum([a,b,cc]) == 1000: 
                print a,b,cc,np.sum([a,b,cc])
		print 'result: ', np.prod([a,b,cc])
                raise MyException()
    #if summe==1000:
    #    break
