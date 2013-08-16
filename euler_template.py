from __future__ import division
doc = """

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

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

ds = {0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'}

dd = ['',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety']
dtens = ['ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']



def wordlength(num):
    l = 0
    literal = str(num).zfill(3)[::-1]
    f = []
    for d in literal:
        f.append(int(d))
    if f[1] != 1:
        l = l + len(ds[f[0]])
        l = l + len( dd[f[1]])
    elif f[1] == 1:
        l = l + len(dtens[f[0]]) 
    if f[2]:
        l = l + len (ds[f[2]] + 'hundred')
        if f[1] or f[0]:
            l = l + len('and')
    if num == 1000:
        l = len("onethousand")
    if num > 1000:
        print 'error! number too big!'
    return l



x = np.arange(1,n+1)
result  = 0
for e in x:
    result = result + wordlength(e)


print 'result:'
print result 
print 'elapsed time:'
print time.time()-start

