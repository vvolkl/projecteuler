
int solve_loop() {
  int a = 1; ///< first fibonacchi number
  int b = 1; ///< second fibonacchi number
  int result = 0;
  const int limit = 4000000;
  while(a < limit && b < limit) {
    a = a + b;
    if (a % 2 == 0) {
      result += a;
    }
    b = a + b;
    if (b % 2 == 0) {
      result += b;
    }
  }
  return result;
}

int result = 0;
const int limit = 4000000;
int fib_rec(int a, int b) {
  if (b > limit) {
    return 0;
  }
  if (b % 2 == 0) { 
    result += b;
  }
  return fib_rec(b, a+b);
}

int solve() {
  fib_rec(1, 1);
  return result;
}

#include "boilermain.cpp"
