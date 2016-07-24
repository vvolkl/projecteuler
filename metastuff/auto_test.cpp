
#include <iostream>


int triple(int input) {
    return 3 * input;
}



int main () {
    int a;
    a = triple(2);
    auto b = triple(3);
    std::cout<<a<<"\t"<<b<<std::endl;

}
