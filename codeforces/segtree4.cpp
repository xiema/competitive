#include <iostream>
#include <map>
#include <utility>
using namespace std;

typedef pair<int, int> pii;
map<int, int> segs;

bool istree(int C) {
  list<pii> seen;
  seen.push_front(make_pair(1, segs[1]));
  int seensz = 1, req_edges = C - 1;
  int i = 2, C2 = 2 * C;
  while (i <= C2) {
    if (seensz == 0) return false;
    auto seg2 = seen.begin();
    if (i == seg2->second) {
      seen.pop_front();
      --seensz;
      ++i;
      continue;
    }

    int seg1 = segs[i];
    auto seen_end = seen.end();
    int last_seen = i;
    while (seg2 != seen_end && seg1 > seg2->second) {
      if (i > seg2->first) {
        last_seen = seg2->first;
        --req_edges;
      } else {
        return false;
      }
      ++seg2;
    }
    seen.insert(seg2, make_pair(last_seen, seg1));
    ++seensz;

    ++i;
  }

  if (req_edges) return false;

  return true;
}

int main () {
  int C, l, r;
  scanf("%d", &C);

  for (int i = 0; i < C; ++i) {
    scanf("%d %d", &l, &r);
    segs[l] = r;
  }

  if (istree(C)) {
    printf("YES");
  }
  else {
    printf("NO");
  }

  return 0;
}
