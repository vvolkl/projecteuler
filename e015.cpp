#include <iostream>

using namespace std;

const int n = 20;


void choose(long int *res, int x, int y){

    if(x < n && y < n){
        choose(res,x+1,y);
        choose(res,x,y+1);
    }
    else{
       *res = *res+1;
    } 
    
    
}
unsigned long nChoosek( unsigned n, unsigned k )
{
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;

    unsigned long result = n;
    for(unsigned int i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}


int main(){

//long int result = 0;
//choose(&result,1,0);
cout<<nChoosek(40,20)<<endl;


}
