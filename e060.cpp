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


// choose set of primes


int main() {
    /*vector<int> a = sieve(1000);
    for (int i=0; i< 50; i++) {
    cout<<a[i]<<endl;
    }
    */

    mpz_t a;
    mpz_init_set_ui(a,1111);
    mpz_t b;
    mpz_init_set_ui(b,2);
    mpz_t temp;
    mpz_init_set_ui(temp,0);

    mpz_out_str(stdout, 10,a);
    cout<<endl<<count_digits(a)<<endl;
    concatenate(temp,a,b);
    mpz_out_str(stdout, 10,temp);
    return  0;
}


