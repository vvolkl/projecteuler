import math as math

def b(n):
  c = -  0.5 * n * (n -1)
  _res = (1 + math.sqrt(1**2 - 4 * c) ) * 0.5
  if abs(math.floor(_res) - _res) < 0.0000000000001:
    b = int(_res)
    if (b -1) * b * 2 == n * (n-1):
      return True
  return False

def b2(n):
  c = -  0.5 * n * (n -1)
  _res = (1 + math.sqrt(1**2 - 4 * c) ) * 0.5
  return _res


found = False
i = 10**12
i = 1000000010724
#i = 40
while found == False:
    print i
    i = i + 1
    found = b(i)
print i
print b2(i)
