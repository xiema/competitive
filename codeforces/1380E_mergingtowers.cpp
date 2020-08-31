#include <iostream>
#include <list>
#include <vector>

using namespace std;

int main() {
  int n,m,a,b,C=0;
  cin >> n >> m;
  vector<int> t(n);
  vector<list<int> > T(m);
  for (int i=0; i<n; ++i) {
    cin >> t[i];
    --t[i];
    T[t[i]].push_back(i);
    if (i>0 && t[i] != t[i-1]) {
      ++C;
    }
  }

  cout << C << '\n';

  for (int i=0; i<m-1; ++i) {
    cin >> a >> b;
    --a,--b;
    if (T[b].size() > T[a].size()) {
      for (auto c : T[a]) {
        if (c>0 && t[c-1] == b) {
          --C;
        }
        if (c<n-1 && t[c+1] == b) {
          --C;
        }
      }
    }
    else {
      for (auto c : T[b]) {
        if (c>0 && t[c-1] == a) {
          --C;
        }
        if (c<n-1 && t[c+1] == a) {
          --C;
        }
      }
    }
    for (auto c : T[b]) {
      t[c] = a;
    }
    T[a].splice(T[a].end(), T[b]);

    cout << C << '\n';
  }



  return 0;
}
