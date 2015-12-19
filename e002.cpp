#include <iostream>

int main() {
  typedef fib_int long int;
  const fib_int upTo = 400000000L;
  fib_int a = 1; 
  fib_int b = 1; 
  fib_int result = 0;
  const 
  while(a < upTo ) {
      std::cerr<<a<<"\t"<<b<<"\t"<<result<<std::endl;
      a = a + b;
      if(a % 2 == 0) {
          result += a;
      }
      b = a + b;
      if(b % 2 == 0) {
          result += b;
      }
  }
  // correct for last term if it went over the limit
  if(b > upTo && b % 2 == 0) {
      result -= b;
  }
  std::cout<<"result: "<<result<<std::endl;
  return 0;
}
