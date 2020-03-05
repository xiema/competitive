#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

struct lecture {
  int id,start,end;
  lecture (int s, int e, int i) {
    id = i;
    start = s;
    end = e;
  }

  bool operator< (const lecture &other) {
    return start < other.start;
  }
};


void make_set(vector<lecture> &ven, unordered_map<int, set<int> > &sens) {
  set<pair<int,int> > ends;
  for (auto iv=ven.begin(); iv!=ven.end(); ++iv) {
    auto ie = ends.begin();
    while (ie!=ends.end() && ie->first < iv->start) {
      ie = ends.erase(ie);
    }
    while (ie!=ends.end()) {
      sens[ie->second].emplace(iv->id);
      sens[iv->id].emplace(ie->second);
      ++ie;
    }
    ends.emplace(iv->end, iv->id);
  }
}


int main () {
  int n;
  vector<lecture> vena,venb;
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    int sa,ea,sb,eb;
    scanf("%d %d %d %d", &sa,&ea,&sb,&eb);
    vena.emplace_back(sa,ea,i);
    venb.emplace_back(sb,eb,i);
  }

  sort(vena.begin(), vena.end());
  sort(venb.begin(), venb.end());

  unordered_map<int, set<int> > sensa, sensb;

  make_set(vena, sensa);
  make_set(venb, sensb);

  bool happy = true;
  for (int i=0; i<n; ++i) {
    auto a = sensa[i].begin();
    auto b = sensb[i].begin();
    while (a != sensa[i].end()) {
      if (*a != *b) {
        happy = false;
        break;
      }
      ++a;
      ++b;
    }
    if (!happy) break;
  }

  if (happy) {
    cout << "YES";
  }
  else {
    cout << "NO";
  }

  return 0;
}
