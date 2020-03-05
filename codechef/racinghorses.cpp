#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Horse{
  int number;
  int strength;
};

bool comp(Horse a, Horse b){
  return a.strength < b.strength;
}

int main(){
  int T;
  cin >> T;
  string out;

  while (T-- > 0){
    int N;
    cin >> N;
    vector<Horse> horses;
    Horse h;
    for (int i=1; i<=N; ++i){
      h.number = i;
      cin >> h.strength;
      horses.push_back(h);
    }
    sort(horses.begin(), horses.end(), comp);

    /*
    for (int i=0; i<N; ++i){
      cout << horses[i].number << ' ' << horses[i].strength << '\n';
    }
    */

    int diff = horses[1].strength - horses[0].strength;
    for (int i=2; i<N; ++i){
      int _diff = horses[i].strength - horses[i-1].strength;
      if (_diff < diff) {
        diff = _diff;
      }
    }

    out = out + to_string(diff) + '\n';
  }

  cout << out;
  return 0;
}
