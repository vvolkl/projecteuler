from __future__ import division
doc = """

Valentin Volkl """

import argparse
import numpy as np
import re
parser = argparse.ArgumentParser(description=doc)
parser.add_argument('n', metavar='n', type=int, nargs='?', default=1000, 
                   help='the main variable for our program')
args = parser.parse_args()
n=args.n

data = np.loadtxt('e011.dat')
maxs = 0
winner = 0
for dat in [data, np.transpose(data)]:
	for row in dat:
		for num in range(np.alen(row[:-3])):
			if maxs < np.prod(row[num:num+4]):
				maxs = np.prod(row[num:num+4])
				winner = row[num:num+4]


for dat in [data, np.rot90(dat)]:
	for i in np.arange(-np.alen(dat[0,:]),np.alen(dat[:,0])):
		#offset = int(i - np.alen(dat[0,:]))
		row= np.diagonal(dat,i)
		print i,row
		if np.alen(row) > 3:
			for num in range(np.alen(row[:-3])):
				print '      ', row[num:num+4]
				if maxs < np.prod(row[num:num+4]):
					maxs = np.prod(row[num:num+4])
					winner = row[num:num+4]
		
print maxs 
print winner

