#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main () {
  int N;
  set<int> pos;
  bool possible;
  while (true) {
    cin >> N;
    if (N==0) break;
    pos.clear();
    possible = true;
    vector<int> v(N);
    for (int c=1;c<=N;++c) {
      int i,d;
      cin >> i >> d;
      int p = c+d;
      if (pos.find(p)!=pos.end() || p < 1 || p > N) {
        possible = false;
      }
      else {
        pos.emplace(p);
        v[p-1] = i;
      }
    }
    if (!possible) {
      cout << -1 << '\n';
    }
    else {
      for (int i=0;i<N;++i) {
        cout << v[i] << (i==N-1 ? '\n' : ' ');
      }
    }
  }

  return 0;
}
