import math as gmpy2
def fermat_factor(n):
    assert n % 2 != 0  # Odd integers only

    a = gmpy2.ceil(gmpy2.sqrt(n))
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n

    factor1 = a + gmpy2.sqrt(b2)
    factor2 = a - gmpy2.sqrt(b2)
    return int(factor1), int(factor2) 

def is_square(n):
    root = gmpy2.sqrt(n)
    return root % 1 == 0  # '4.0' will pass, '4.1212' won't
a = 1001
c=999
while(a>1000):
	c=c-1	
	d = 1000 * c + int(str(c)[::-1])
	

	a,b =fermat_factor(d)
	print d,a,b 


