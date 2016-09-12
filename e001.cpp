#include "Eigen/Dense"

template <typename T>
T sumMultiples(T A, T B, T upTo) {
  T result = 0;
  for(T i=0; i < upTo; ++i) {
    if ( !(i % A) || !(i % B)) {
      result += i;
    }
  }
  return result;
}


int solve() {
   int A = 3;
   int B = 5;
   int upTo = 1000;
   int result = sumMultiples<int>(A, B, upTo);
  return result;
}

#include "boilermain.cpp"
