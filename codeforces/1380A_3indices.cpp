#include <iostream>

using namespace std;

int main() {
  int T,n,i,j,k,iv,jv,p;

  cin >> T;

  while (T--) {
    cin >> n;
    i=0,j=0,k=0;
    for (int a=1; a<=n; ++a) {
      cin >> p;
      if (i==0) {
        i = a;
        iv = p;
      }
      else if (j==0) {
        if (p > iv) {
          j = a;
          jv = p;
        }
        else if (p < iv) {
          i = a;
          iv = p;
        }
      }
      else if (k==0) {
        if (p < jv) {
          k = a;
        }
        else if (p > jv) {
          j = a;
          jv = p;
        }
      }
    }

    if (k) {
      cout << "YES\n" << i << ' ' << j << ' ' << k << '\n';
    }
    else {
      cout << "NO\n";
    }
  }

  return 0;
}
