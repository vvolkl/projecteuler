#include <iostream>
#include "math.h"
using namespace std;

int main() {
  // input to be decomposed in primes 
  const double n = 600851475143;
  cout<<"looking for prime factors of "<<n<<"..."<<endl;
  double remainder = 0.1;
  // divisor
  double i = 2;

  while(ceilf(remainder) != remainder) {
    remainder = n / i;
    i++;
    cout<<i<<":\t"<<remainder<<"\t"<<ceilf(remainder)<<endl;
  }
  cout.precision(11);
  cout<<"largest prime factor:   "<<remainder<<endl;
  return 0;
}
