#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

int gcf(int a, int b){
  if (a == b) {
    return a;
  } else if (a == 1 || b == 1){
    return 1;
  }

  if (a > b){
    return gcf(a-b, b);
  } else {
    return gcf(b-a, a);
  }
}

int main(){
  string s;
  int id, per;
  set<pii> queries;
  int itv = 0;

  while (true){
    cin >> s;
    if (s == "#") break;
    if (s == "Register"){
      cin >> id >> per;
      queries.emplace(per, id);
      if (itv == 0) itv = per;
      else itv = gcf(itv, per);
    }
  }

  int c,t=0;
  cin >> c;
  while (c > 0){
    t+=itv;
    for (auto it = queries.begin(); it != queries.end(); ++it){
      if (t%it->first == 0) {
        cout << it->second << '\n';
        --c;
      }
    }
  }
  return 0;
}
