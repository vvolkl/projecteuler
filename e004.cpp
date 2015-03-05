#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int isPalindrome(int candidate) {
    string s1 = to_string(candidate);
    string s2 = s1;
    reverse(s1.begin(), s1.end());
    return s1 == s2;
}

int main() {
    int factor1, factor2, result, palindromeCandidate;
    result = 1;
    for (factor1 = 999; factor1 > 1; factor1--) {
        for (factor2 = 2; factor2 < factor1; factor2++) {
            palindromeCandidate = factor1 * factor2;
            //cout << "\t" << palindromeCandidate << endl;
            if (isPalindrome(palindromeCandidate)) {
                result = max(result, palindromeCandidate);
            }   
        }
    }
    cout << result << "\t" << factor1 << "\t" << factor2 << endl;
    return 0;
}
