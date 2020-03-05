#include <bits/stdc++.h>
using namespace std;

int p2[31];

int g(int n, int k){
  if (n == 1){
    return k;
  } else if (k >= p2[n-1]) {
    return g(n-1, p2[n]-k-1) + p2[n-1];
  } else {
    return g(n-1, k);
  }
}

int main(){
  for (int i=0; i<32; ++i){
    p2[i] = pow(2, i);
  }

  int N,n,k;
  cin >> N;
  while (N-- > 0){
    cin >> n >> k;
    cout << g(n,k) << '\n';
  }
  return 0;
}
