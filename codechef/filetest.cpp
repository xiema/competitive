#include <fstream>
#include <iostream>
using namespace std;

const string fn = "filetest.cpp";

int main(){
  ifstream f_in;
  f_in.open(fn);
  string s;
  while (getline(f_in, s)) {
    cout << s << endl;
  }
  return 0;
}
