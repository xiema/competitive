#include <bits/stdc++.h>
using namespace std;

int main(){
  int N, M;
  while (true){
    cin >> N >> M;
    if (N == 0 && M == 0){
      break;
    }
    set<int> jack, jill;
    vector<int> both;
    while (N--){
      int n;
      cin >> n;
      jack.insert(n);
    }
    while (M--){
      int n;
      cin >> n;
      jill.insert(n);
    }
    set_intersection(jack.begin(), jack.end(), jill.begin(), jill.end(), back_inserter(both));
    cout << both.size() << '\n';
  }
  return 0;
}
