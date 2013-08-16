#include <iostream>
#include <cmath>
#define N 500 

//using namespace std;

int main(){
    
    int total = 0;
    int i = 0;
    int j = 0;
    long int trinum = 0;
   
    float r =0.5;
    while(total <= N ){
        ++i;
        trinum += i;
        total = 1;
        for(j = 1; j < trinum / 2 + 1; ++j ){
            r = (double) trinum / j;
            if(r == ceilf(r)){
                ++total;
                //std::cout<<trinum<<'\t'<<j<<'\t'<<r<<'\t'<<floor(r)<<std::endl;
            
            }
        }        
        std::cout<<trinum<<'\t'<<total<<std::endl;
        

    }
    

std::cout<<total<<'\t'<<trinum<<std::endl;
    return(0); 
}
