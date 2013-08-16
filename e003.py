from __future__ import division


doc="""Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Valentin Volkl 28.6.2013"""

import sys



try:
	n = int(sys.argv[1])
except:
	n = 600851475143

d = int(n / 2)

while (n % d):
	d = d - 1
print 'solution:', d
	
