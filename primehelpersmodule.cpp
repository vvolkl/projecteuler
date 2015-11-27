#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <gmp.h> 

#include "primehelpersmodule.h"

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
    //size_t max_range = (size_t) floor(sqrt(prime));
    vector<int> candidates(prime);
    vector<int> primes;
    for(int i=0; i < prime; i++) {
        candidates[i] = i;
    }
    int p = 2;
    primes.push_back(p);
    int k = 1;
    bool done = 0;
    while(p < prime) { 
        //cout<<" "<<candidates[11]<<endl;    
        for(int i = p; i < prime; i = i + p) {
                //cout<<"setting candidate to zero:  \t"<<i<<"\t"<<p<<endl;
                candidates[i] = 0;
            }
        while(!done && p < prime) {
            //cout<<p<<"\t"<<candidates[p]<<endl;
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
    cout << "Hello " <<  name << "!\n";
}
 
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/class.hpp>
#include <boost/python/copy_const_reference.hpp>
#include <boost/python/return_by_value.hpp>
#include <boost/python/return_value_policy.hpp>
#include <boost/python/to_python_converter.hpp>
#include <boost/python/list.hpp>


using namespace boost::python;
 

template<class T>
struct VecToList
{
    static PyObject* convert(const vector<T>& vec)
    {
        list* l = new list();
        for(size_t i = 0; i < vec.size(); i++)
            (*l).append(vec[i]);
        return l->ptr();
    }
};

BOOST_PYTHON_MODULE(primehelpers_cpp)
{
    //to_python_converter<vector<int,allocator<int> >, VecToList<int> >();
    to_python_converter<std::vector<int, std::allocator<int> >, VecToList<int> >();
    def("checkTwoPrimes", checkTwoPrimes);
    def("sieve", sieve );//, return_value_policy<return_by_value>());
}

