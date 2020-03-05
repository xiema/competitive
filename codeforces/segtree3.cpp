#include <iostream>
#include <list>
#include <unordered_set>
#include <stack>
#include <utility>
using namespace std;

typedef pair<int, int> pii;
const int sz = 1e6+10;
int segs[sz];
unordered_set<int> edges[sz];
bool visited[sz];

bool istree(int C) {
  list<pii> seen;
  seen.push_front(make_pair(1, segs[1]));
  int seensz = 1, req_edges = C - 1;
  int i = 2, i_end = 2*C;

  if (C == 1) return true;
  if (segs[1] == i_end) return false;

  while (i <= i_end) {
    if (seensz == 0 || req_edges < 0) return false;
    auto seg2 = seen.begin();
    if (i == seg2->second) {
      seen.pop_front();
      --seensz;
      ++i;
      continue;
    }

    int seg1 = segs[i];
    if (seg1 == i+1) return false;
    auto seen_end = seen.end();
    int last_seen = i;

    if (seg1 == i_end) {
      int last_seen = i;
      while (true) {
        if (seg2 == seen_end) {
          if (seg1-1 != last_seen) {
            i_end = seg1-1;
          }
          break;
        }
        else if (i > seg2->first) {
          if (seg2->second-1 != last_seen)
            i_end = seg2->second-1;
          last_seen = seg2->second;
          --req_edges;
          edges[seg1].emplace(last_seen);
          edges[seg2->second].emplace(seg1);
        } else {
          return false;
        }
        ++seg2;
      }
    }
    else {
      while (seg2 != seen_end && seg1 > seg2->second) {
        if (i > seg2->first) {
          last_seen = seg2->second;
          --req_edges;
          edges[seg1].emplace(last_seen);
          edges[last_seen].emplace(seg1);
        } else {
          return false;
        }
        ++seg2;
      }
      seen.insert(seg2, make_pair(last_seen, seg1));
    }
    ++seensz;

    ++i;
  }

  if (req_edges) return false;

  int count = 0;
  stack<int> next( {i_end} );
  while (!next.empty()) {
    int v1 = next.top();
    next.pop();
    if (!visited[v1]) {
      ++count;
      visited[v1] = true;
      for (auto v2 = edges[v1].begin(); v2 != edges[v1].end(); ++v2) {
        if (!visited[*v2]) {
          next.push(*v2);
        }
      }
    }
  }

  if (count == C) return true;

  return false;
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
