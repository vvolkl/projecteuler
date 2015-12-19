#include <iostream>

int main() {
  long int a = 1; 
  long int b = 1; 
  long int result = 0;
  while(a < 4000000L ) {
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
  // correct for last term if it is already over the limit
  if(b > 4000000L && b % 2 == 0) {
      result -= b;
  }
  std::cout<<"result: "<<result<<std::endl;
  std::cerr<<!(b % 2)<<"\t"<<!b%2<<std::endl;


  std::cout<<sizeof(result)<<std::endl;
  return 0;
}
