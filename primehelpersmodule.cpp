#include <iostream>
#include <vector>
#include <math.h>
#include <gmp.h> 
using namespace std;
 



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

vector<int> sieve(int prime) {
    //Naive implementation of Erastosthenes' sieve.
    size_t max_range = (size_t) floor(sqrt(prime));
    vector<int> candidates(prime);
    vector<int> primes(max_range);
    
    for(int i=0; i < prime; i++){
        candidates[i] = i;
    }
    int p = 2;
    primes[0] = p;
    int k = 1;
    bool done = 0;
    while(p < max_range) { 
        //cout<<" "<<candidates[11]<<endl;    
        for(int i = p; i < prime; i++) {
            if (i%p == 0) {
                cout<<"\t"<<i<<"\t"<<p<<endl;
                candidates[i] = 0;
                }
            }
        while(!done && p < prime) {
            p = p + 1;
            //cout<<p<<"\t"<<candidates[p]<<endl;
            if (candidates[p] != 0) {
                primes[k] = p;
                k = k + 1;
                done = 1; 
            }
        }
        done = 0;
    }
    return primes;
}




int checkTwoPrimes(int aa, int bb) {
    mpz_t a;
    mpz_init_set_ui(a, aa);
    mpz_t b;
    mpz_init_set_ui(b, bb);

    int result = 1;
    mpz_t temp;
    mpz_init_set_ui(temp,0);
    concatenate(temp, a, b);
    result  = result  * mpz_probab_prime_p(temp,25);
    concatenate(temp,b,a);
    result  = result  * mpz_probab_prime_p(temp,25);
    return result;
}
void say_hello(const char* name) {
    cout << "Hello " <<  name << "!\n";
}
 
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(primehelpers)
{
    def("checkTwoPrimes", checkTwoPrimes);
}

