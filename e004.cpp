#include <string>
#include <algorithm>


using namespace std;

int isPalindrome(int candidate) {
    string s1 = to_string(candidate);
    string s2 = s1;
    reverse(s1.begin(), s1.end());
    return s1 == s2;
}
/** print solution to project euler problem 4
    finds the largest palindronic number that is a product of two three-digit numbers.
    Algorithm:
      Check if the product is palindronic for every combination of factors
**/

int solve() {
    int factor1, factor2, result, palindromeCandidate;
    result = 1;
    for (factor1 = 999; factor1 > 1; factor1--) {
        for (factor2 = 2; factor2 < factor1; factor2++) {
            palindromeCandidate = factor1 * factor2;
            if (isPalindrome(palindromeCandidate)) {
                result = max(result, palindromeCandidate);
            }   
        }
    }
    return result;
}

#include "boilermain.cpp"
