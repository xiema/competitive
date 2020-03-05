#include <iostream>
#include <queue>
#include <forward_list>
#include <list>
#include <unordered_map>
#include <utility>
using namespace std;

typedef long long ll;

struct triple {
  int first, second, third;
  triple (int a, int b, int c) {
    first = a;
    second = b;
    third = c;
  }
};

int main () {
  int T, k, k2, root;
  int a,b,t,c;
  unordered_map<int, list<pair<int,int> > > houses;
  unordered_map<int, int> sizes;
  unordered_map<int, bool> flg;
  forward_list<triple> houselist;
  queue<int> q;

  scanf("%d", &T);
  while (T--) {
    scanf("%d", &k);
    k2 = 2 * k;
    for (int i=0; i<k2-1; ++i) {
      scanf("%d %d %d", &a, &b, &t);
      houses[a].emplace_back(b, t);
      houses[b].emplace_back(a, t);
    }

    for (auto iter = houses.begin(); ; ++iter) {
      if (iter->second.size() == 1) {
        root = iter->first;
        break;
      }
    }

    q.push(root);
    flg[root] = true;
    c = 1;
    while (!q.empty()) {
      a = q.front();
      list<pair<int, int>> blist = houses[a];
      for (auto iter = houses[a].begin(); iter != houses[a].end(); ++iter) {
        b = iter->first, t = iter->second;
        if (!flg[b]) {
          houselist.emplace_front(b, a, t);
          q.push(b);
          flg[b] = true;
          ++c;
        }
      }
      q.pop();
    }

    ll tmax = 0, tmin = 0;
    for (auto iter = houselist.begin(); iter != houselist.end(); ++iter) {
      b = iter->first, a = iter->second, t = iter->third;
      int szb = sizes[b] + 1;
      tmax += (ll)min(szb, k2-szb) * t;
      sizes[a] += szb;
      if (flg[b]) {
        flg[a] = !flg[a];
        tmin += t;
      }
    }

    printf("%lld %lld\n", tmin, tmax);

    houses.clear();
    sizes.clear();
    flg.clear();
    houselist.clear();
  }

  return 0;
}
