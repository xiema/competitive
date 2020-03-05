#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> va(n);
  vector<int> vt(n);
  for (int i=0;i<n;++i) {
    cin >> va[i];
  }
  for (int i=0;i<n;++i) {
    cin >> vt[i];
  }

  int lo = va[0], hi = va[0];
  unordered_map<int, multiset<int> > m;
  for (int i=0;i<n;++i) {
    m[va[i]].emplace(-vt[i]);
    lo = min(lo, va[i]);
    hi = max(hi, va[i]);
  }

  multiset<int> q;
  int total = 0, c = lo;
  while (!q.empty() || c <= hi) {
    if (m.find(c)!=m.end()) {
      for (auto t : m[c]) {
        q.emplace(t);
      }
    }
    if (!q.empty()) q.erase(q.begin());
    for (auto t : q) {
      total += t;
    }
    ++c;
  }

  cout << -total << '\n';

  return 0;
}
