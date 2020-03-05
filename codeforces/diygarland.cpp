#include <iostream>
#include <list>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> pii;

const int sz = 2e5+10;
int counts[sz];
int imps[sz];

int main () {
  int n;
  list<pii> rank;
  int root;
  bool first = true;

  scanf("%d", &n);
  for (int i=1; i<n; ++i) {
    int l;
    scanf("%d", &l);
    rank.push_front(make_pair(l, counts[l]));
    ++counts[l];
    imps[l] = l;
    if (first) {
      root = l;
      first = false;
    }
  }

  priority_queue<pii, vector<pii>, greater<pii> > lamps;
  for (int i=1; i<=n; ++i) {
    if (counts[i] == 0) {
      lamps.push(make_pair(i, i));
      imps[i] = i;
    }
  }

  bool possible = true;
  list<pii> wires;

  for (auto itr = rank.begin(); itr!=rank.end(); ++itr) {
    if (lamps.empty()) {
      possible = false;
      break;
    }
    pii l = lamps.top();
    lamps.pop();
    wires.emplace_back(itr->first, l.second);
    if (itr->second == 0) {
      pii p = make_pair(max(imps[itr->first], l.first), itr->first);
      lamps.push(p);
    } else {
      imps[itr->first] = max(imps[itr->first], l.first);
    }
  }

  ///*
  if (possible) {
    printf("%d\n", root);
    for (auto itw = wires.begin(); itw != wires.end(); ++itw) {
      printf("%d %d\n", itw->first, itw->second);
    }
  }
  else {
    printf("-1\n");
  }
  //*/

  return 0;
}
