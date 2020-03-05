#include <iostream>
#include <list>
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
int* graphs[sz];

bool istree(int C) {
  int vertices = 0, edges = 0;
  list<Segment> cur;
  int graph = 0;

  ///*
  auto segsend = segs+C;
  for (int i = 0; i < C; ++i) {
    Segment seg1 = segs[i];
    auto curend = cur.end();
    for (auto seg2 = cur.begin(); seg2 != curend; ) {
      if (seg2->right > seg1.left) {
        if (seg1.right > seg2->right) {
          ++edges;
          if (graphs[seg1.index] != NULL) {
            if (graphs[seg2->index] != NULL) {
              if (*graphs[seg1.index] == *graphs[seg2->index]) {
                return false;
              }
              *graphs[seg2->index] = *graphs[seg1.index];
            }
            else {
              graphs[seg2->index] = graphs[seg1.index];
              ++vertices;
            }
          }
          else {
            if (graphs[seg2->index] != NULL) {
              graphs[seg1.index] = graphs[seg2->index];
              ++vertices;
            }
            else {
              int* g;
              *g = graph++;
              graphs[seg1.index] = g;
              graphs[seg2->index] = g;
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
    cur.emplace_back(seg1);
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
