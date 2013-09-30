// projecteuler.net
// Valentin Volkl

#include <iostream>

using namespace std;

int main(int argc, char *argv[]){

int result = 0;
for(int i = 0; i < 1000;++i){
    if(! (i % 3) || (i % 5)){
        result += i;
    }
}
cout<<"result: "<<endl;
cout<<result<<endl;

return 0;
}

