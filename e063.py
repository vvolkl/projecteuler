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

######## 

n = 1
found_one = True
while  n < 100 :
    curr_result = result
    for i in range(1,100):
        print n, i**n,  len(str(i**n))
        if len(str(i**n))>n:
            n = n + 1
            break
        if len(str(i**n)) == n:
            result = result + 1
    if result == curr_result:
        found_one = False
    


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

