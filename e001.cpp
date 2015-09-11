/* projecteuler.net
/ Valentin Volkl
/ TODO: implement improvement from projecteulerpdf
/ add all numbers divisible by 3 and 5 and subtract
/ numbers divisible by 15
*/

#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
  long int N, result;
  if ( argc > 1) {
    N = std::atoi(argv[1]);
  } else {
    N = 1000;
  }
  std::cout<<"summing multiples of 3 and 5 up to "<<N<<"..."<<std::endl;
  for(long int i=0; i < N; ++i) {
    if ( !(i % 3) || (i % 5)) {
      result += i;
    }
  }
  std::cout<<"result: "<<std::endl;
  std::cout<<result<<std::endl;
  return 0;
}

