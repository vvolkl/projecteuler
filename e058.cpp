#include <iostream>
#include <gmp.h>

using namespace std;

int main(){
    unsigned int primes = 3;
    unsigned int  all_diag= 5;
    mpz_t diag_entry;
    mpz_init_set_ui(diag_entry,9);
    unsigned int side=4;
    while (all_diag <= 10*primes) {
 //   while(side < 8){
    for (int i =0;i<4; i++){

        mpz_add_ui(diag_entry, diag_entry, side);
        mpz_out_str(stdout,10,diag_entry);
        cout<<endl;
        if( mpz_probab_prime_p(diag_entry,25)){
            primes += 1;
        }
        all_diag ++;
    }
    cout<<"\t"<<primes<<"\t/ "<<all_diag<<endl;
    side = side + 2;  
  
    
    }
    
    cout<<"result (side length): \t"<<side-1<<endl;
    return 0;
}
