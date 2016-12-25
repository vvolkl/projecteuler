

unsigned long nChoosek (unsigned n, unsigned k) {
  if (k > n) return 0;
  if (k * 2 > n) k = n-k;
  if (k == 0) return 1;

  unsigned long result = n;
  for(unsigned int i = 2; i <= k; ++i ) {
    result *= (n-i+1);
    result /= i;
  }
  return result;
}

unsigned long int solve(){
  return nChoosek(40,20);
}

#include "boilermain.cpp"
