#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <gmp.h> 

#include "primehelpersmodule.h"

namespace Primes {

  int count_digits(mpz_t num) {
      int c = 0;
      mpz_t temp;
      mpz_init_set(temp, num);
      while (mpz_cmp_ui(temp, 1) > 0) {
          mpz_cdiv_q_ui(temp,  temp, 10);
          c++;
      }
      return c;
  }

  void concatenate(mpz_t temp, mpz_t a, mpz_t b) {
      mpz_set(temp,a);
      mpz_t temp2;
      mpz_init_set(temp2, b);
      mpz_mul_ui(temp2, b, pow(10, count_digits(a)));
      mpz_add(temp,a,temp2 );
      //mpz_out_str(stdout, 10,temp);
  }

  std::vector<int> sieve(int prime) {
      //Naive implementation of Erastosthenes' sieve.
      //size_t max_range = (size_t) floor(sqrt(prime));
      std::vector<int> candidates(prime);
      std::vector<int> primes;
      for(int i=0; i < prime; i++) {
          candidates[i] = i;
      }
      int p = 2;
      primes.push_back(p);
      int k = 1;
      bool done = 0;
      while(p < prime) { 
          //std::cout<<" "<<candidates[11]<<std::endl;    
          for(int i = p; i < prime; i = i + p) {
                  //std::cout<<"setting candidate to zero:  \t"<<i<<"\t"<<p<<std::endl;
                  candidates[i] = 0;
              }
          while(!done && p < prime) {
              //std::cout<<p<<"\t"<<candidates[p]<<std::endl;
              p = p + 1;
              if (candidates[p] != 0) {
                  primes.push_back(p);
                  k = k + 1;
                  done = 1; 
              }
          }
          done = 0;
      }
      primes.pop_back();
      return primes;
  }

  int checkTwoPrimes(int aa, int bb) {
      mpz_t a;
      mpz_init_set_ui(a, aa);
      mpz_t b;
      mpz_init_set_ui(b, bb);

      int result = 1;
      mpz_t temp;
      mpz_init_set_ui(temp, 0);
      concatenate(temp, a, b);
      result  = result  * mpz_probab_prime_p(temp, 25);
      concatenate(temp, b, a);
      result  = result  * mpz_probab_prime_p(temp, 25);
      return result;
  }

  void say_hello(const char* name) {
      std::cout << "Hello " <<  name << "!\n";
  }

} // namespace Primes
