#include <iostream>
#include <vector>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iterator>
using namespace std;

int main () {
  int n,m;
  scanf("%d %d", &n, &m);
  list<int> cur;
  for (int i=1; i<=n; ++i) {
    cur.push_back(i);
  }

  vector<vector<int> > states;
  unordered_set<int> seen;
  states.emplace_back(cur.begin(), cur.end());

  for (int i=0; i<m; ++i) {
    int msg;
    scanf("%d", &msg);
    auto it = find(cur.begin(), cur.end(), msg);
    rotate(cur.begin(), it, next(it));
    states.emplace_back(cur.begin(), cur.end());
    seen.emplace(msg);
  }

  /*
  for (auto it1=states.begin(); it1!=states.end(); ++it1) {
    for (auto it2=it1->begin(); it2!=it1->end(); ++it2) {
      cout << *it2 << ' ';
    }
    cout << '\n';
  }
  */

  unordered_map<int, int> maxpos;
  int i = m, j = n-1;
  int c = 0;
  while (c < n) {
    //cout << i << ' ' << j << ' ' << states[i][j] << '\n';
    if (maxpos.find(states[i][j]) == maxpos.end()) {
      maxpos[states[i][j]] = j+1;
      ++c;
    }
    --i;
    if (i < 0) {
      i = m;
      --j;
    }
  }

  for (int i=1; i<=n; ++i) {
    int a = seen.count(i) > 0 ? 1 : i;
    int b = maxpos[i];
    printf("%d %d\n", a,b);
  }

  return 0;
}
