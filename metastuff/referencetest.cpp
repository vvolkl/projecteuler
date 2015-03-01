#include<iostream>
#include <typeinfo>
int func(int &num) {
    num = num + 1;
    return num;
}

int main() {
    int a = 5;
    int &b = a;
    std::cout <<"now a is: " << a << ", "  << func(a) << "\t""and a is : " << a << std::endl;
    return 0;
}
