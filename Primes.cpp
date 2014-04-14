#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

vector<int> sieve(int prime){
    
    int max_range = floor(sqrt(prime));
    vector<int> candidates(max_range);
    vector<int> primes(max_range);
    
    for(int i=0; i < max_range; i++){
        candidates[i] = i+2;
    }
    int p = 2;
    bool done = 0;
    while(!done){ 
        for(int i=0; i < maxrange; i++  ){
            
            }
        }
    return primes;
}
int main()

    vector<int> a = sieve(100);
    cout<<a[0]<<endl;
    return  0;
}


