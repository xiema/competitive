#include <iostream>
#include <unordered_map>
#include <list>
#include <array>
#include <utility>
#include <algorithm>
using namespace std;

struct Segment {
  int left, right, index;

  Segment () {
    
  }

  Segment (int l, int r, int i) {
    left = l;
    right = r;
    index = i;
  }

  bool operator < (const Segment& other) const {
    return left < other.left;
  }
};

const int sz = 5e5 + 10;
Segment segs[sz];

bool istree(int C) {
  int vertices = 0, edges = 0;
  unordered_map<int, int*> graphs;
  list<Segment> cur;
  int graph = 0;

  ///*
  auto segsend = segs+C;
  for (auto seg1 = segs.begin(); seg1 != segsend; ++seg1) {
    auto curend = cur.end();
    for (auto seg2 = cur.begin(); seg2 != curend; ) {
      if (seg2->right > seg1->left) {
        if (seg1->right > seg2->right) {
          ++edges;
          auto seg1_g = graphs.find(seg1->index);
          auto seg2_g = graphs.find(seg2->index);
          auto graphs_end = graphs.end();
          if (seg1_g != graphs_end) {
            if (seg2_g != graphs_end) {
              if (*(seg1_g->second) == *(seg2_g->second)) {
                return false;
              }
              *(seg2_g->second) = *(seg1_g->second);
            }
            else {
              graphs.insert(make_pair(seg2->index, seg1_g->second));
              ++vertices;
            }
          }
          else {
            if (seg2_g != graphs_end) {
              graphs.insert(make_pair(seg1->index, seg2_g->second));
              ++vertices;
            }
            else {
              int* g;
              g = new int(graph);
              graphs.insert(make_pair(seg1->index, g));
              graphs.insert(make_pair(seg2->index, g));
              ++graph;
              vertices += 2;
            }
          }
        }
        ++seg2;
      }
      else {
        seg2 = cur.erase(seg2);
      }
    }
    cur.emplace_back(*seg1);
  }
  //*/

  //printf("%d %d\n", vertices, edges);

  if (vertices == 0 || vertices-1 == edges) {
    return true;
  }

  return false;
}

int main () {
  int C, l, r;
  scanf("%d", &C);

  for (int i = 0; i < C; ++i) {
    scanf("%d %d", &l, &r);
    segs[i] = Segment(l, r, i);
  }

  sort(segs, segs+C);

  if (istree(C)) {
    printf("YES");
  }
  else {
    printf("NO");
  }

  return 0;
}
