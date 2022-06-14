#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  int T,N,fuel,i,j,x;
  vector<int> trk;

  cin >> T;
  for (int c=1;c<=T;++c) {
    cin >> N;
    trk.clear();
    for (i=0;i<N;++i) {
      cin >> x;
      trk.push_back(x);
    }
    for (i=0;i<N;++i) {
      cin >> x;
      trk[i] -= x;
    }
    fuel = 0;
    i = 0;
    j = 0;
    while (i < N && j < trk.size()) {
      fuel += trk[j];
      while (fuel < 0) {
        fuel -= trk[i];
        trk.push_back(trk[i]);
        i+=1;
      }
      j+=1;
    }
    if (i >= N) {
      cout << "Case " << c << ": Not possible\n";
    }
    else {
      cout << "Case " << c << ": Possible from station " << i+1 << '\n';
    }
  }
  return 0;
}
