from __future__ import division
doc = """


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714. What is the total of all the name scores in the file?

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

names = []
result = 0
with open('e022_names.txt') as f:
    a = f.read()
    names = a.replace('"','').split(',')
if args.verbose:
    print len(names)
    print names[1:10]
names = sorted(names)
if args.verbose:
    print len(names)
    print names[1:10]     
i = 0
for e in names:
    wordscore  = 0
    i = i + 1
    for char in e:
        wordscore = wordscore + ord(char) - 64
    if args.verbose:
        print i,e,wordscore,result    
    result = result  + wordscore * i

print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

