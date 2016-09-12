#include <iostream>
#include "math.h"
using namespace std;

int main() {
  // input to be decomposed in primes 
  double n = 600851475143;
  double remainder = 0.1;
  // divisor
  long int factor = 1;

  while(n > 1) {
    ++factor;
    if (static_cast<long int>(n) % factor == 0) {
      n = static_cast<long int>(n / static_cast<double>(factor));
    }
  }
  cout<<factor<<endl;
  return 0;
}
