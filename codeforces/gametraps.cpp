#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <utility>
using namespace std;

struct trap {
  int loc,disarm,danger;
  trap (int l, int d, int da) {
    loc = l;
    disarm = d;
    danger = da;
  }

  bool operator< (const trap &other) {
    return danger < other.danger;
  }
};

int main () {
  int m,n,k,t;
  vector<int> soldiers;
  vector<trap> traps;

  scanf("%d %d %d %d", &m, &n, &k, &t);
  for (int i=0; i<m; ++i) {
    int sa;
    scanf("%d", &sa);
    soldiers.push_back(sa);
  }

  for (int i=0; i<k; ++i) {
    int l,r,d;
    scanf("%d %d %d", &l, &r, &d);
    traps.emplace_back(l,r,d);
  }

  sort(traps.rbegin(), traps.rend());
  t-=n+1;
  list<pair<int,int> > disarmed;
  int minlevel = 0;
  auto i_trap = traps.begin();
  while (true){
    if (i_trap == traps.end()) {
      minlevel = 0;
      break;
    }
    minlevel = i_trap->danger;
    int a = i_trap->loc, b = i_trap->disarm;
    auto i_dis = upper_bound(disarmed.begin(), disarmed.end(), make_pair(a,b));
    if (i_dis != disarmed.begin()) {
      --i_dis;
      if (a <= i_dis->second ) {
        t+= 2*(i_dis->second-i_dis->first+1);
        a = i_dis->first;
        b = max(i_dis->second, b);
        i_dis = disarmed.erase(i_dis);
      }
      else {
        ++i_dis;
      }
    }
    while (i_dis != disarmed.end()) {
      if (i_dis->first <= b) {
        t+= 2*(i_dis->second-i_dis->first+1);
        b = max(b, i_dis->second);
        i_dis = disarmed.erase(i_dis);
      }
      else {
        break;
      }
    }
    t -= 2*(b-a+1);
    if (t < 0) {
      break;
    }
    disarmed.insert(i_dis, make_pair(a,b));

    ++i_trap;
  }

  int count = 0;
  for (auto i_s = soldiers.begin(); i_s != soldiers.end(); ++i_s) {
    if (*i_s >= minlevel) {
      ++count;
    }
  }

  //cout << minlevel << '\n';
  cout << count;

  return 0;
}
