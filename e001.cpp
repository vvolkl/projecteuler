// projecteuler.net
// Valentin Volkl
// TODO: implement improvement from projecteulerpdf
// add all numbers divisible by 3 and 5 and subtract 
// numbers divisible by 15

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
  long int N;
  if ( argc > 1) {
    N = atoi(argv[1]);
  } else {
    N = 1000;
  }
  cout<<"summing multiples of 3 and 5 up to "<<N<<"..."<<endl;
  long int result = 0;
  for(long int i=0; i < N; ++i) {
    if ( !(i % 3) || (i % 5)) {
      result += i;
    }
  }
  cout<<"result: "<<endl;
  cout<<result<<endl;
  return 0;
}

