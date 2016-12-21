
//#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
//#include "catch.hpp"
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

/*
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
*/
/*
SCENARIO( "Factors are computed") {
  REQUIRE(factors(9)[0] == 3);
  REQUIRE(factors(9)[1] == 3);
  REQUIRE(factors(12)[0] == 2);
  REQUIRE(factors(12)[1] == 2);
  REQUIRE(factors(12)[2] == 3);
  REQUIRE(factors(12).size() == 3);
}
*/

int factorSum(int num) {
  int result = 1;
  int _t = 0;
  for (int i = 2; i < num/2 + 1; ++i) {
    _t = 1;
	  while ( num % i == 0 ) {
      _t *=i;
      num /= i;
			result += _t;
		}
    if (num == 1) {
      return result;
    }
  }
  return result;
}
/*
SCENARIO("Test summation of proper divisors of a number") {
  REQUIRE(factorSum(2) == 1);
  REQUIRE(factorSum(2) == 1);
  REQUIRE(factorSum(4) == 3);
  REQUIRE(factorSum(6) == 6);
  REQUIRE(factorSum(12) == 16);
}
*/
bool isAbundant(int num) {
  return factorSum(num) > num;
}
/*
SCENARIO("Test check if number is abundant") {
  REQUIRE(isAbundant(12) == true);
  REQUIRE(isAbundant(11) == false);
  REQUIRE(isAbundant(1) == false);
}
*/

std::vector<int> getAllAbundantNumbers(int upTo=23861) {
  std::vector<int> abundantNumbers;
  abundantNumbers.reserve(upTo);
  for (int i = 12; i < upTo; i++) {
    std::cout<<"."<<i;
    if (isAbundant(i)) {
      abundantNumbers.push_back(i);
    }
  }
  std::cout<<"end"<<std::endl;
  return abundantNumbers;
}
/*
SCENARIO( "Test method to find all abundant numbers in range" ) {
  REQUIRE(getAllAbundantNumbers(13)[0] == 12);
}
*/

std::vector<int> aSums(const std::vector<int>& numbers) {
  std::vector<int> sums;
  for (auto i = numbers.begin(); i != numbers.end(); ++i) {
    for (auto j = numbers.begin(); j != i + 1; ++j) {
      sums.push_back(*i + *j);
    }
  }
  std::sort(sums.begin(), sums.end());
  auto it = std::unique(sums.begin(), sums.end());
  sums.resize( std::distance(sums.begin(),it));
  return sums;

}
/*
SCENARIO("Test custom summation method") {
  std::vector<int> numbers {1, 2, 3};
  std::vector<int> result = aSums(numbers);
  REQUIRE(result.size() == 5);
  REQUIRE(result[0] == 2);
  REQUIRE(result[1] == 3);
  REQUIRE(result[2] == 4);
  REQUIRE(result[3] == 5);
  REQUIRE(result[4] == 6);
}
*/


int solve() {
  std::cout <<"asdf"<<std::endl;
  int upTo = 23861;
  std::cout <<"asdf"<<std::endl;
  std::vector<int> abundantNumbers = getAllAbundantNumbers(upTo);
  std::cout <<"asdf"<<std::endl;
  auto sums = aSums(abundantNumbers);
  std::cout <<"asdf"<<std::endl;
  auto sums_end = std::remove_if(sums.begin(), sums.end(), [=](int x) {return x > upTo;});
  std::cout <<"asdf"<<std::endl;
  sums.erase(sums_end, sums.end());
  std::cout <<"asdf"<<std::endl;
  std::vector<int> allNumbers(upTo);
  std::iota(allNumbers.begin(), allNumbers.end(), 1);
  std::cout <<"iota"<<std::endl;
  std::vector<int> notSums;
  std::set_symmetric_difference(
    sums.begin(), sums.end(),
    allNumbers.begin(), allNumbers.end(),
    std::back_inserter(notSums));
  return std::accumulate(notSums.begin(), notSums.end(), 0);

}



#include "boilermain.cpp"





