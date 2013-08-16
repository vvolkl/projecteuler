from __future__ import division
doc = """

Valentin Volkl """

import argparse
import numpy as np

parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000, 
                   help='the main variable for our program')
args = parser.parse_args()

#print args.n
n=args.n

print -np.sum(np.arange(1,n+1)**2) + np.sum(np.arange(1,n+1))**2


