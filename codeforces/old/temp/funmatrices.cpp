#include <iostream>
#include <string>
using namespace std;

int main () {
  int T,N;
  int mtx[9][9];
  int temp;
  char c;

  cin >> T;

  for (int C=1;C<=T;++C) {
    cin >> N;
    for (int i=0;i<N;++i) {
      for (int j=0;j<N;++j) {
        cin >> c;
        mtx[i][j] = c-'0';
      }
    }

    int M;
    bool flipped = false;
    cin >> M;
    while (M--) {
      string s;
      cin >> s;
      switch (s[0]) {
        case 'r':
        case 'c':
          int a,b;
          cin >> a >> b;
          if ((!flipped && s[0]=='c') || (flipped && s[0]=='r')) {
            for (int i=0;i<N;++i) {
              temp = mtx[i][a-1];
              mtx[i][a-1] = mtx[i][b-1];
              mtx[i][b-1] = temp;
            }
          }
          else {
            for (int i=0;i<N;++i) {
              temp = mtx[a-1][i];
              mtx[a-1][i] = mtx[b-1][i];
              mtx[b-1][i] = temp;
            }
          }
          break;
        case 't':
          flipped = !flipped;
          break;
        case 'i':
          for (int i=0;i<N;++i) {
            for (int j=0;j<N;++j) {
              mtx[i][j] = (mtx[i][j]+1)%10;
            }
          }
          break;
        case 'd':
          for (int i=0;i<N;++i) {
            for (int j=0;j<N;++j) {
              mtx[i][j] = (mtx[i][j]+9)%10;
            }
          }
          break;
      }
    }

    cout << "Case #" << C << '\n';

    if (!flipped) {
      for (int i=0;i<N;++i) {
        for (int j=0;j<N;++j) {
          cout << mtx[i][j];
        }
        cout << '\n';
      }
    }
    else {
      for (int i=0;i<N;++i) {
        for (int j=0;j<N;++j) {
          cout << mtx[j][i];
        }
        cout << '\n';
      }
    }

    cout << '\n';
  }

  return 0;
}
