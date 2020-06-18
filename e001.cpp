
int solve() {
  long int result = 0;
  for(long int i = 0; i < 1000; ++i) {
    if (!(i % 3) || !(i % 5)) {
      result += i;
    }
  }
  return result;
}

#include "boilermain.cpp"
