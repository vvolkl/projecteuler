
def fib_recursive(a, b, result, n):
  if b > n:
    return result
  a = a + b
  b = a - b
  if (a % 2 == 0):
    result += a
  return fib_recursive(a, b, result, n)


def solve(n=4e6):
  result = 0
  return fib_recursive(1, 0, result, n)
  
