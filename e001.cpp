#include<iostream>
#include<string>
//#include"e001.h" 


template <typename t1>
t1 sum_multiples_of(t1 A, t1 B, t1 upTo) {
  t1 result = 0;
  for(t1 i=0; i < upTo; ++i) {
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
   int result =  sum_multiples_of<int>(A, B, upTo);
  return result;

}
int main(int argc, char *argv[]) {
  int result = solve();
  std::cout<<result<<std::endl;
}

