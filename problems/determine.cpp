#include <iostream>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

typedef long long ll;

map<pair<ll, ll>, ll> vals;
ll n;

ll func (pair<ll, ll> p) {
  if (vals.find(p) != vals.end()) {
    return vals[p];
  }
  ll i = p.first, j = p.second;
  if (i >= j) {
    ll r1 = 0, r2 = 0;
    if (i < n) {
      for (ll k = i+1; k <= n; ++k) {
        r1 = max(r1, func(make_pair(k,1)) + func(make_pair(k,j)));
      }
    }
    if (j > 1) {
      for (ll k = 1; k < j; ++k) {
        r2 = max(r2, func(make_pair(i,k)) + func(make_pair(n,k)));
      }
    }
    ll r = r1 + r2;
    vals[p] = r;
    return r;
  }
  else {
    ll r = 0;
    for (ll k = i; k < j; ++k) {
      r = max(r, func(make_pair(i,k)) + func(make_pair(k+1,j)));
    }
    vals[p] = r;
    return r;
  }
}

int main () {
  ll a;
  while (cin >> n >> a) {
    vals[make_pair(n,1)] = a;
    cout << func(make_pair(1,n)) << '\n';
    vals.clear();
  }
}
