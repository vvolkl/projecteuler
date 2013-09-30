#include <iostream>
using namespace std;

int main(int argc, char *argv[]){

int a; int b; 
a = b = 1;
int result = 0;
while(a < 4000 * 1000){
    cerr<<a<<"\t"<<b<<"\t"<<result<<endl;
    a = a + b;
    if(a % 2 == 0){
        result += a;
    }
    b = a + b;
    if(b % 2 == 0){
        result += b;
    }
}
if(b > 4000 * 1000 && b %2 == 0){
    result -=b;
}
cout<<"result: "<<result<<endl;
cerr<<!(b % 2)<<"\t"<<!b%2<<endl;


return 0;
}
