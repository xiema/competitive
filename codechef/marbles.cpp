#include <iostream>
#include <cmath>
using namespace std;

long long c(int n, int r){
  if (r > n-r)
    r = n-r;
  long long res = 1;
  for (int i=1; i<=r; ++i){
    res *= n - r + i;
    res /= i;
  }

  return res;
}

int main(){
  int T,n,k;
  cin >> T;
  string out;

  while (T-- > 0){
    cin >> n >> k;
    n -= k;
    out = out + to_string(c(n+k-1, n)) + '\n';
  }

  cout << out;
  return 0;
}
