#include <bits/stdc++.h>
using namespace std;

int main(){
  int N, Q;
  while (cin >> N >> Q){
    map<int, vector<int> > positions;
    for (int i=1; i<=N; ++i){
      int n;
      cin >> n;
      positions[n].push_back(i);
    }
    for (int i=0; i<Q; ++i){
      int k,v,pos;
      cin >> k >> v;
      if (k <= positions[v].size()){
        pos = positions[v][k-1];
      } else {
        pos = 0;
      }
      cout << pos << '\n';
    }
  }
  return 0;
}
