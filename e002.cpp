#include <iostream>

template <typename typeT>
typeT evenFibonacci_straightforward(typeT upTo) {
  typeT a = 1;
  typeT b = 1;
  typeT result = 0;
  while (a < upTo) {
    a = a + b;
    // keep only even terms
    if (a % 2 == 0) {
      result += a;
    }
    b = a + b;
    if (b % 2 == 0) {
      result += b;
    }
  }
  //correct for last term if it is already over the limit
  if (b > upTo && b % 2 == 0) { 
    result -= b;
  }
  return result;
}

long int solve() {
  return evenFibonacci_straightforward(
    40000000L);
}

