/*
Problem 119
===========


The number 512 is interesting because it is equal to
the sum of its digits raised to some power: 
5 + 1 + 2 = 8, and 8^3 = 512. 
Another example of a number with this property is 
614656 = 28^4.

We shall define a[n] to be the nth term of this sequence
and insist that a number must contain at least two digits
to have a sum.

You are given that a[2] = 512 and a[10] = 614656.

Find a[30].


Answer: 72fddfa6c52a120892ade628f3819da4
*/

/* Brute force solution:
For each n, find the sum of the digits
and raise it successively until it is either equal to 
or exceeds the original number.
  */


#include <vector>
#include <string>
#include <iostream>

inline int sum_of_digits(const int num) {
  int result = 0;
  std::string s = std::to_string(num);
  for(char const &c: s) {
    result += c - 48;
  }
  return result;
}

int solve () {
  std::vector<int> results;
  int i = 0;
  long int n = 10;
  long int sd2;
  long int sd;
  while(results.size() < 31) {
    sd2 = sum_of_digits(n);
    sd = sd2; 

    if (sd != 1){
    while (sd < n) {
      sd = sd * sd2;
    }
    if (n == 512) {
    std::cout << "found: " << i << "\t" << n << "\t" << sd2 << "\t" << sd << std::endl;
    }

    //std::cout << n << "\t" << sd2 << "\t" << sd << std::endl;
    if ( sd == n) {
      i++;
    results.push_back(n);

    std::cout << "found: " << i << "\t" << n << "\t" << sd2 << "\t" << sd << std::endl;
    }

    }
  n = n+1;

  }
  return n;
  }



int main() {
  std::cout << sum_of_digits(1234507) << std::endl;
  solve();
  return 1;
}


