#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef vector<int> vi;
typedef vector<set<int> > vsi;
typedef long long ll;

vi a,b,c;
vi r0,r1;
vsi T;

ll dfs(int u, int p, int m) {
  ll M = 0;
  m = min(m, a[u]);
  for (auto v : T[u]) {
    if (v == p) continue;
    M += dfs(v, u, m);
    r0[u] += r0[v];
    r1[u] += r1[v];
  }
  if (b[u] != c[u]) {
    if (c[u]) {
      ++r1[u];
    } else {
      ++r0[u];
    }
  }
  ll d = min(r0[u], r1[u]);
  r0[u]-=d; r1[u]-=d;

  return M + 2*d*m;
}

int main() {
  int n;

  cin >> n;
  for (int i=0; i<n; ++i) {
    int ai,bi,ci;
    cin >> ai >> bi >> ci;
    a.push_back(ai);
    b.push_back(bi);
    c.push_back(ci);
    r0.push_back(0);
    r1.push_back(0);
    T.emplace_back();
  }

  for (int i=1; i<n; ++i) {
    int u,v;
    cin >> u >> v;
    T[u-1].emplace(v-1);
    T[v-1].emplace(u-1);
  }

  ll M = dfs(0,-1,a[0]);
  if (r0[0] || r1[0]) M = -1;

  cout << M << endl;

  return 0;
}
