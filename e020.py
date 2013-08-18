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
args = parser.parse_args()
n=args.n

import math
digits = str(math.factorial(n))
result = reduce(lambda x,y: x+y, [int(d) for d in digits])

start = time.time()
print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

