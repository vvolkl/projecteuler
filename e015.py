from __future__ import division
doc = """
<p>Starting in the top left corner of a 2&times;2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.</p>
<div style="text-align:center;">
<img src="project/images/p_015.gif" alt="" />
</div>
<p>How many such routes are there through a 20&times;20 grid?</p>

Valentin Volkl """

import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=20, 
                   help='the main variable for our program')
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
n=args.n
start = time.time()

#grid = np.zeros( (n+1,n+1) )
#print grid
def choose(x,y):
    if args.verbose:
        print x,y
    global result
    if x < n and y < n:
        choose(x+1,y)
        choose(x,y+1)
    else:
        result = result + 1
        if args.verbose:
            print 'intermed. result:', result
            print 'Endpoint'

   # if y < n:
   #     result = result + 1
       
result = 0
choose(1,0)
print 'result:'
print result 
print 'elapsed time:'
print time.time()-start
