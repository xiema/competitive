#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int N1,N2,N3,total;
  string out;

  cin >> N1 >> N2 >> N3;
  total = N1 + N2 + N3;
  int voters[total];
  for (int i=0; i<total; ++i){
    cin >> voters[i];
  }
  sort(voters, voters+total);

  int cur = voters[0];
  int b = false;
  int c = 0;
  for (int i=1; i<total; ++i){
    if (voters[i] == cur){
      if (!b) {
        b = true;
        out = out + to_string(cur) + '\n';
        ++c;
      }
    } else {
      cur = voters[i];
      b = false;
    }
  }

  cout << to_string(c) << '\n' << out;
  return 0;
}
