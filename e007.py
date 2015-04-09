from __future__ import division
import argparse
import numpy as np

doc = ''
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=20, 
                   help='scaling variable')
args = parser.parse_args()
n = args.n

from primehelpers_cpp import sieve

print sieve(10000000)[1000]

