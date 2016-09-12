
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <vector>


int handleOneFactor(std::vector<int>& factors, int factor, int num) {
  while ( num % factor == 0 ) {
    num /= factor;
    factors.push_back(factor);
  }
  return num;
}

std::vector<int> factors(int num) {
  std::vector<int> factors;
  num = handleOneFactor(factors, 2, num);
  for (int i = 3; i < num + 1; i+=2) {
    num = handleOneFactor(factors, i, num);
    if (num == 1) {
      return factors;
    }
  }
}

SCENARIO( "Factors are computed") {
  REQUIRE(factors(9)[0] == 3);
  REQUIRE(factors(9)[1] == 3);
  REQUIRE(factors(12)[0] == 2);
  REQUIRE(factors(12)[1] == 2);
  REQUIRE(factors(12)[2] == 3);
  REQUIRE(factors(12).size() == 3);
}

