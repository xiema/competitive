#include <iostream>
#include <set>
using namespace std;

void diff(set<int> &s1, set<int> &s2) {
  for (auto it=s2.begin(); it!=s2.end(); ++it) {
    auto _it = s1.find(*it);
    if (_it!=s1.end()) {
      s1.erase(_it);
    }
  }
}

void isct(set<int> &s1, set<int> &s2) {
  for (auto it=s1.begin(); it!=s1.end();) {
    if (s2.find(*it)!=s2.end()) {
      ++it;
    }
    else {
      it = s1.erase(it);
    }
  }
}

int main() {
  int M;
  set<int> coins_lt,coins_gt;
  set<int> pa,pb;
  cin >> M;
  while (M--) {
    int N,K;
    cin >> N >> K;
    coins_lt.clear();
    coins_gt.clear();
    for (int i=1; i<= N; ++i) {
      coins_lt.emplace(i);
      coins_gt.emplace(i);
    }
    while (K--) {
      pa.clear();
      pb.clear();
      int c,p;
      cin >> c;
      for (int i=0; i<c; ++i) {
        cin >> p;
        pa.emplace(p);
      }
      for (int i=0; i<c; ++i) {
        cin >> p;
        pb.emplace(p);
      }
      char op;
      cin >> op;
      if (op == '>') {
        isct(coins_lt,pb);
        isct(coins_gt,pa);
      }
      else if (op == '<') {
        isct(coins_lt,pa);
        isct(coins_gt,pb);
      }
      else if (op == '=') {
        diff(coins_lt,pb);
        diff(coins_lt,pa);
        diff(coins_gt,pb);
        diff(coins_gt,pa);
      }
    }


    if (coins_lt.size() == 1 && coins_gt.size() == 0) {
      cout << *coins_lt.begin() << '\n';
    }
    else if (coins_gt.size() == 1 && coins_lt.size() == 0) {
      cout << *coins_gt.begin() << '\n';
    }
    else if (coins_gt.size() == 1 && coins_lt.size() == 1 && *coins_lt.begin()==*coins_gt.begin()) {
      cout << *coins_gt.begin() << '\n';
    }
    else {
      cout << 0 << '\n';
    }

    if (M > 0) cout << '\n';
  }
  return 0;
}
