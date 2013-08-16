doc="""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


28.07.13 Valentin Volkl
"""

import sys
import numpy as np
try:
	n = int(sys.argv[1])
except:
	n = 1000


print doc
d = np.arange(0,n,1)
print 'solution:', np.sum(d[(d % 3 == 0) + (d % 5 == 0)])

