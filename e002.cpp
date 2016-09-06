#include <iostream>

int main() {
    int a = 1; 
    int b = 1; 
    int result = 0;
    while(a < 4000 * 1000) {
        std::cerr<<a<<"\t"<<b<<"\t"<<result<<std::endl;
        a = a + b;
        if(a % 2 == 0) {
            result += a;
        }
        b = a + b;
        if(b % 2 == 0) {
            result += b;
        }
    }
    // correct for last term if it is already over the limit
    if(b > 4000 * 1000 && b % 2 == 0) {
        result -= b;
    }
    std::cout<<result<<std::endl;
    return 0;
}
