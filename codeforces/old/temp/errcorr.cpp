#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  while (cin >> n) {
    if (n == 0) break;
    vector<int> sum;
    for (int i=0; i<n; ++i)
      sum.push_back(0);
    int x;
    int rowerr = -1;
    bool corrupt = false;
    for (int i=0; i<n; ++i) {
      int rowsum = 0;
      for (int j=0; j<n; ++j) {
        cin >> x;
        sum[j] += x;
        rowsum += x;
      }
      if (rowsum%2) {
        if (rowerr >= 0) {
          corrupt = true;
        }
        rowerr = i;
      }
    }
    int colerr = -1;
    if (!corrupt) {
      for (int i=0; i<n; ++i) {
        if (sum[i]%2) {
          if (colerr >= 0) {
            corrupt = true;
          }
          colerr = i;
        }
      }
    }
    if (corrupt) {
      cout << "Corrupt\n";
    }
    else if (colerr == -1 and rowerr == -1) {
      cout << "OK\n";
    }
    else if (colerr >= 0 and rowerr >= 0) {
      cout << "Change bit (" << rowerr+1 << "," << colerr+1 << ")\n";
    }
    else {
      cout << "Corrupt\n";
    }
  }
  return 0;
}
