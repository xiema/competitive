#include <iostream>
using namespace std;

int main(){
  int A, N, K;
  cin >> A >> N >> K;
  ++N;
  for (int i=0; i<K; ++i){
    cout << A % N << ' ';
    A /= N;
  }
  return 0;
}
