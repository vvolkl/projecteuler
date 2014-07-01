#include <iostream>
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

int main() {

    mpz_t q;
    mpz_init_set_ui(q,3);
    mpz_t qprime;
    mpz_init_set_ui(qprime, 1);
    
    mpz_t d;
    mpz_init_set_ui(d ,2);
   
    mpz_t _q;
    mpz_init_set_ui(_q,0);
    
    mpz_t _d;
    mpz_init_set_ui(_d,0);
    
    int a,b;
    int result = 0;
    for (int i = 0; i < 1000; i++) {
        mpz_add(_d,   q, d);
        
        mpz_add(_q,  _d, d);
        
        mpz_set(d,_d);
        mpz_set(q, _q);
        mpz_sub(qprime,  q, d);
        
        //mpz_out_str(stdout, 10, q);
        //cout<<" / ";
        //mpz_out_str(stdout, 10, d);
        a = count_digits(q);
        b = count_digits(d);
        result += (a > b);
        cout<<a<<"\t"<<b<<"\t"<<result<<endl;
        //cout<<"\t"<<endl<<mpz_sizeinbase(q,10)<<"\t"<<mpz_sizeinbase(d,10)<<endl;
        
    }

    cout<<"result: \t"<<result<<endl;
    return 0;
}

