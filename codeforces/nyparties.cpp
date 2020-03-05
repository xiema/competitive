#include <iostream>
#include <unordered_set>
#include <list>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;


int main () {
  int n, f;

  scanf("%d", &n);
  vector<int> friends;
  while (n--) {
    scanf("%d", &f);
    friends.push_back(f);
  }

  sort(friends.begin(), friends.end());
  int occ_max = 0, occ_min = 0;
  int start = friends[0], possible_occ = 0, count = 0;
  int end = start;
  list<pair<int, int> > groups;
  unordered_set<int> occ;

  for (auto itf = friends.begin(); itf != friends.end(); ++itf) {
    if (*itf > end+1) {
      if (possible_occ > 1) {
        if (occ.find(start-1) == occ.end()) {
          occ.emplace(start-1);
          ++occ_max;
        }
        if (occ.find(end+1) == occ.end()) {
          occ.emplace(end+1);
          ++occ_max;
        }
      }
      else if (possible_occ > 0) {
        groups.push_back(make_pair(start, end));
      }
      int add = end-start+1;
      occ_max += add;
      if (add < 3) {
        ++occ_min;
      }
      else {
        occ_min += add/3;
        if (add%3) ++occ_min;
      }
      start = *itf;
      end = start;
      count = 1;
      possible_occ = 0;
    }
    else {
      if (end == *itf) {
        ++count;
        if (count > 1) {
          ++possible_occ;
        }
      }
      else {
        count = 1;
      }
      end = *itf;
    }
  }

  if (possible_occ > 1) {
    if (occ.find(start-1) == occ.end()) {
      occ.emplace(start-1);
      ++occ_max;
    }
    if (occ.find(end+1) == occ.end()) {
      occ.emplace(end+1);
      ++occ_max;
    }
  }
  else if (possible_occ > 0) {
    groups.push_back(make_pair(start, end));
  }
  int add = end-start+1;
  occ_max += add;
  if (add < 3) {
    ++occ_min;
  }
  else {
    occ_min += add/3;
    if (add%3) ++occ_min;
  }

  for (auto itg = groups.begin(); itg != groups.end(); ++itg) {
    if (occ.find((itg->first)-1) == occ.end()) {
      occ.emplace((itg->first)-1);
      ++occ_max;
    }
    else if (occ.find((itg->second)+1) == occ.end()) {
      occ.emplace((itg->second)+1);
      ++occ_max;
    }
  }

  printf("%d %d", occ_min, occ_max);

  return 0;
}
