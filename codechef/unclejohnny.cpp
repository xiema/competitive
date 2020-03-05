#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int T, N, songs[100], K, Klen, pos;
  string out;
  cin >> T;

  while (T-- > 0){
    cin >> N;
    for (int i=0; i<N; ++i){
      cin >> songs[i];
    }
    cin >> K;
    Klen = songs[K-1];

    pos = 1;
    for (int i=0; i<N; ++i){
      if (songs[i] < Klen) ++pos;
    }

    out = out + to_string(pos) + '\n';
  }

  cout << out;
  return 0;
}
