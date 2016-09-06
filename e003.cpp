#include <iostream>
#include "math.h"
using namespace std;

int main() {
  // input to be decomposed in primes 
  const double n = 600851475143;
  double remainder = 0.1;
  // divisor
  double i = 2;

  while(ceilf(remainder) != remainder) {
    remainder = n / i;
    i++;
  }
  cout.precision(11);
  cout<<remainder<<endl;
  return 0;
}
