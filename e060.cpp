#include <vector>
#include <algorithm>
#include <iostream>

#include "primehelpersmodule.h"

std::vector<int> intersect1d( 
    std::vector<int> v1, 
    std::vector<int> v2) {
  std::vector<int> result(v1.size());
  std::vector<int>::iterator it;
    it = std::set_intersection(
      v1.begin(), 
      v1.end(), 
      v2.begin(), 
      v2.end(),
      result.begin());
    result.resize(it - result.begin());
  return result;
}

int main() { 
  int n = 1200;
  int result = 0;
  auto primes = Primes::sieve(n*n);
  std::vector<std::vector<int>> checkTable(n);
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (Primes::checkTwoPrimes(primes[i], primes[j])) {
          checkTable[i].push_back(j);
          checkTable[j].push_back(i);
      }
    }
  }
  std::cout<<"generated checkTable!"<<std::endl;
  std::vector<int> primelist_intersection1;
  std::vector<int> primelist_intersection2;
  std::vector<int> primelist_intersection3;
  std::vector<int> primelist_intersection4;
  for (int p1 = 0; p1 < n; p1++) {
    for (auto p2: checkTable[p1]) {
      primelist_intersection1 = intersect1d(checkTable[p1], 
                                           checkTable[p2]);
      for (auto p3: primelist_intersection1) {
        primelist_intersection2 = intersect1d(primelist_intersection1, 
                                              checkTable[p3]);
        for (auto p4: primelist_intersection2) {
          primelist_intersection3 = intersect1d(primelist_intersection2, 
                                                checkTable[p4]);
          for (auto p5: primelist_intersection3) {
            for (auto pp: {p1, p2, p3, p4, p5}) {
              std::cout<<primes[pp]<<"\t";
              result += primes[pp];
            }
            std::cout<<std::endl;
            std::cout<<"result: "<<result<<std::endl;
            return 0;
          }
        }
      } 
    }
  }
  return 1; // exit -- nothing found
}
