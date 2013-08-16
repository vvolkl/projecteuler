#include <iostream>

using namespace std;

const int n = 20;


void choose(long int *res, int x, int y){

    if(x < n && y < n){
        //cout<<x<<"\t"<<y<<endl;
        choose(res,x+1,y);
        choose(res,x,y+1);
    }
    else{
       *res = *res+1;
    } 
    
    
}


int main(){

long int result = 0;
choose(&result,1,0);
cout<<"result:\t"<<2*result<<endl;


}
