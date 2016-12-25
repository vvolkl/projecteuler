
int solve() {
  /// input to be decomposed in primes 
  double n = 600851475143;
  long int factor = 1;

  while(n > 1) {
    ++factor;
    if (static_cast<long int>(n) % factor == 0) {
      n = static_cast<long int>(n / static_cast<double>(factor));
    }
  }
  return factor;
}

#include "boilermain.cpp"
