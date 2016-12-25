
int solve() {
  int a = 1; ///< first fibonacchi number
  int b = 1; ///< second fibonacchi number
  int result = 0;
  const int limit = 4000000;
  while(a < limit) {
    a = a + b;
    if (a % 2 == 0) {
      result += a;
    }
    b = a + b;
    if (b % 2 == 0) {
      result += b;
    }
  }
  // correct for last term if it is already over the limit
  if(b > limit && b % 2 == 0) {
    result -= b;
  }
  return result;
}

#include "boilermain.cpp"
