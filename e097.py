
def solve():
  num = 1
  for i in range(7830457):
    num = (num * 2)  % 10000000000
  return (num * 28433 + 1) % 10000000000
