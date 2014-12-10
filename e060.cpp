#include <Python.h>

#include <iostream>
#include <vector>
#include <math.h>
#include <gmp.h>


PyMODINIT_FUNC
initdemo(void)
{
    PyObject *m;

    m = Py_InitModule("spam", SpamMethods);
    if (m == NULL)
        return;

    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    Py_INCREF(SpamError);
    PyModule_AddObject(m, "error", SpamError);
}



static PyObject *
demo_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    sts =5; 
    return Py_BuildValue("i", sts);
}


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




int checkTwoPrimes(mpz_t a, mpz_t b) {
    int result = 1;
    mpz_t temp;
    mpz_init_set_ui(temp,0);
    concatenate(temp, a, b);
    result  = result  * mpz_probab_prime_p(temp,25);
    concatenate(temp,b,a);
    result  = result  * mpz_probab_prime_p(temp,25);
    return result;
}

// choose set of primes


int main() {
    /*vector<int> a = sieve(1000);
    for (int i=0; i< 50; i++) {
    cout<<a[i]<<endl;
    }
    */

    mpz_t a;
    mpz_init_set_ui(a,7);
    mpz_t b;
    mpz_init_set_ui(b,109);
    mpz_t temp;
    mpz_init_set_ui(temp,0);

    mpz_out_str(stdout, 10,a);
    cout<<endl<<count_digits(a)<<endl;
    concatenate(temp,a,b);
    mpz_out_str(stdout, 10,temp);

    cout<<endl<<endl;
    cout<<checkTwoPrimes(a,b)<<endl;

    return  0;
}


