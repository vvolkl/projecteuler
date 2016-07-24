#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void foo() {
  static int counter = 0;
  cout << "foo has been called " << ++counter << " times\n";
}

int readWriteTextFile(string filename) {
    cout << "> trying to open file " << filename << endl;
    ifstream file (filename) ;
    string line;
    while ( getline(file, line) ) {
        cout << ">" << line << endl;
    }
    file.close();
    ofstream file2(filename, ofstream::app);
    file2 << "This line was appended by a program!" << endl;
    file2.close();
    return 0;
}
 
int main() {
  cout << "--- reference test ..." << endl;
  for( int i = 0; i < 10; ++i ) foo();
  cout << "--- file io test..." << endl;
  readWriteTextFile("testtext.txt");
  return 0;
}
