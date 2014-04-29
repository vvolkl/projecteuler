#include<iostream>
#include<algorithm>
#include<vector>
#include <gmp.h>


//TODO: handle big integers
using namespace std;

vector<int> separate_into_digits(mpz_t value ) {
    vector<int> digits ;
    for( ; value > 0 ; value /= 10 ) digits.push_back( value%10 ) ;
    reverse( digits.begin(), digits.end() ) ;
    return digits ;
    }

int int_from_vector(vector<int> vec, bool reverse) {
    int res;
    int off = 1;
    if (reverse) {
        for (int i=vec.size()-1;i>-1;i--) {
            res += vec[i] * off;
            off *= 10;
        
        }
    }
    else {
        for (int i=0;i< vec.size(); i++) {
            res += vec[i] * off;
            off *= 10;
        
        }
    }
    return res;
}

bool is_palindrome(vector<int> vec) {
    int j = vec.size() - 1;    
    for (int i = 0; i < vec.size() / 2; i++){
        if (vec[i] != vec[j]){
            return 0;
        }
    j--;
    }
    return 1;

}




int main() {

    cout<<"<<<<<<<<<<<<<<<TEST"<<endl;
    int t = 1234567890;
    int p = 733337;
    vector<int> v = separate_into_digits(t);
    cout<<int_from_vector(v,0)<<endl;
    cout<<int_from_vector(v,1)<<endl;
    cout<<t<<endl<<is_palindrome(separate_into_digits(t))<<endl;
    cout<<p<<endl<<is_palindrome(separate_into_digits(p))<<endl;


cout<<">>>>>>>>>>>>>>>TEST:"<<endl;


    int num_lychrel = 0;
    mpz_t  temp = 0;
    vector<int> digits;
    for (unsigned int i = 0; i<351; ++i) {
        temp = 0; 
        digits = separate_into_digits(i);
        
        //create new number array   

        int j = 0;
        int done = 0;
        cerr<<"checking "<<i<<endl;
        while(j<50 && done == 0){
            //iterate and check if Lychrel
            //iterate()
            //done = check_lycrel()
            cerr<<"\t"<<temp;
            temp = int_from_vector(digits,0) + int_from_vector(digits,1);
            cerr<<"\t"<<temp<<endl;
            digits = separate_into_digits(temp);
            done = is_palindrome(digits);
            j++;
            }
        if (done == 0) {
            cout<<"found lychrel number :\t"<<i<<endl;
            num_lychrel++;
        }

        }

    cout<<num_lychrel<<endl;
    return 0;
}
