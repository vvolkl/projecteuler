
int solve() {
  int result = 0;
  for(int i=0; i < 1000; ++i) {
    if (!(i % 3) || !(i % 5)) {
      result += i;
    }
  }
  return result;
}

#include "boilermain.cpp"
