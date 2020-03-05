#include <iostream>
using namespace std;

int main(){
  string s, out;
  int T, N, start, count;
  cin >> T;

  while (T-- > 0){
    cin >> N >> s;
    start = 0;
    count = 0;
    while (start < N){
      if (s[start] == '1'){
        ++count;
        for (int i=start+1; i < N; ++i){
          if (s[i] == '1')
            ++count;
        }
      }
      ++start;
    }

    out = out + to_string(count) + '\n';
  }

  cout << out;
  return 0;
}
