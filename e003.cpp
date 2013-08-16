#include <iostream>
#include "math.h"
using namespace std;

int main(){

const double n = 600851475143;
//const double n = 105;
cout<<n<<endl;
double d = n / 2;
//cout<<d<<endl;
double remainder = 0.1;
double i = 2;
cout<<n/i<<endl;
while(ceilf(remainder)!=remainder){
  	remainder = n / i;
	//remainder -= int(remainder); 
	i++;
	cout<<i<<":  "<<remainder<<"  "<<ceilf(remainder)<<endl;
}
cout.precision(11);
cout<<"solution:   "<<remainder<<endl;

return 0;
}
