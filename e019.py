from __future__ import division
doc = """

Valentin Volkl """
import argparse
import numpy as np
import re
import time
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000, 
                   help='the main variable for our program')
args = parser.parse_args()
n=args.n


start = time.time()

import datetime
start_date = datetime.date(1901,1,1)
end_date = datetime.date(2000,12,31)
result = 0
for n in range(int ((end_date - start_date).days) + 1):
    curr = start_date + datetime.timedelta(n)
    if curr.weekday() == 6 and curr.day == 1:
        result = result + 1

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

