#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<long long> A(N), x(N), y(N);
  for (int i=0; i<N; ++i) {
    cin >> A[i];
  }
  x[0] = -1;
  for (int i=1; i<N; ++i) {
    int j = i-1;
    while (j>=0  && A[j] <= A[i]) {
      j=x[j];
    }
    x[i]=j;
  }
  y[N-1] = N;
  for (int i=N-2; i>=0; --i) {
    int j = i+1;
    while (j<N && A[j] <= A[i]) {
      j=y[j];
    }
    y[i]= j;
  }
  for (int i=0; i<N; ++i) {
    cout << (x[i]>=0 ? x[i]+1 : -1) + (y[i]<N ? y[i]+1 : -1) << ' ';
  }
  return 0;
}
