#include <iostream>

using namespace std;

const int LIMIT = 1e4;
const int NLIMIT = 5e5;
int p[LIMIT];
bool c[LIMIT];
int pc = 0;

void gen_primes() {
  for (int i=2; i<LIMIT; ++i) {
    if (c[i]) continue;
    p[pc++] = i;
    int j = i+i;
    while (j < LIMIT) {
      c[j] = true;
      j += i;
    }
  }
}

int main() {
  gen_primes();

  int n;
  cin >> n;
  int l[NLIMIT];
  for (int i=0; i<n; ++i){
    int a;
    cin >> a;

    if (!c[a]) {
      l[i] = -1;
      cout << -1 << ' ';
      continue;
    }

    bool A = false;
    for (int j=0; j<pc; ++j) {
      if (p[j] > a) break;
      if (a%p[j]) continue;
      int d1 = 1,d2 = a;
      while (d2%p[j] == 0) {
        d2/=p[j];
        d1*=p[j];
      }
      if (d2 != 1) {
        l[i] = d2;
        A = true;
        cout << d1 << ' ';
        break;
      }
    }

    if (!A) {
      l[i] = -1;
      cout << -1 << ' ';
    }
  }

  cout << endl;
  for (int i=0; i<n; ++i)
    cout << l[i] << ' ';

  return 0;
}
