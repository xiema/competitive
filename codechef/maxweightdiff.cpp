#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
  int T, N, K, W[100], diff;
  string out;
  cin >> T;

  while (T-- > 0){
    cin >> N >> K;
    for (int i=0; i<N; ++i){
      cin >> W[i];
    }
    sort(W, W+N);

    /*
    for (int i=0; i<N; ++i){
      cout << W[i] << ' ';
    }
    */

    diff = 0;
    for (int i=0; i<N; ++i){
      if (i < K){
        diff -= W[i];
      } else {
        diff += W[i];
      }
    }

    out = out + to_string(abs(diff)) + '\n';
  }

  cout << out;
  return 0;
}
