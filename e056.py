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

from __future__ import division
doc = """

Valentin Volkl """

import numpy as np
import re
import time

start = time.time()
result = 0

######## 

def digitsum(num):
    num = str(num)
    s = 0
    for e in num:
        s += int(e)
    return s

for a in range(100):
    for b in range(100):
        result = max(result, digitsum(a**b))


print 'result:'
print result
print 'elapsed time:'
print time.time()-start



print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

