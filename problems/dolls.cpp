#include <bits/stdc++.h>
using namespace std;

bool comp (const pair<int, int>& p1, const pair<int, int>& p2) {
  if (p1.first == p2.first) {
    return p1.second < p2.second;
  }
  return p1.first > p2.first;
}

int main() {
  int T, C, w, h;
  cin >> T;
  while (T--) {
    int C;
    cin >> C;
    vector<pair<int, int> > dolls;
    for (int i = 0; i < C; ++i) {
      cin >> w >> h;
      dolls.emplace_back(w, h);
    }
    sort(dolls.begin(), dolls.end(), comp);

    vector<pair<int, int> > stacks;
    for (auto _doll = dolls.begin(); _doll != dolls.end(); ++_doll) {
      bool b = false;
      for (auto _stk = stacks.begin(); _stk != stacks.end(); ++_stk) {
        if (_stk->first > _doll->first && _stk->second > _doll->second) {
          b = true;
          _stk->first = _doll->first;
          _stk->second = _doll->second;
          break;
        }
      }
      if (!b) {
        stacks.push_back(*_doll);
      }
    }

    cout << stacks.size() << '\n';
  }
}
