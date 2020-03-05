#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

typedef long long ll;
ll limit = 1e9+7;

int main () {
  int T, n;
  ll total, mult, suf, add, _total;
  char ch;
  bool b;
  list<int> ints;
  scanf("%d\n", &T);

  while (T--) {
    scanf("%d\n", &n);
    total = 0;
    while (true) {
      ch = getchar();
      if (ch == '\n' || ch == '$') break;
      ints.push_back(ch-'0');
      ++total;
    }
    b = true;
    auto iter = ints.begin();
    for (int k=0; k<n; ++k) {
      mult = *iter-1;
      suf = total-k-1;
      add = mult * suf;
      _total = total + add;
      if (b) {
        if (_total > n) {
          auto ia = next(iter);
          auto ib = ints.end();
          ll c = n-total;
          for (ll i=0; i<c; ++i) {
            ints.push_back(*ia);
            if (++ia == ib) ia = next(iter);
          }
          b = false;
        }
        else {
          auto ia = next(iter);
          auto ib = ints.end();
          for (ll i=0; i<add; ++i) {
            ints.push_back(*ia);
            if (++ia == ib) ia = next(iter);
          }
        }
      }
      total = _total % limit;
      ++iter;
    }

    printf("%d\n", total);

    ints.clear();
  }

  return 0;
}
