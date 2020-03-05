#include <iostream>
#include <string>
using namespace std;

bool check(string &s, string &a, string &b, int si, int ai, int bi) {
  if (ai >= a.length() && bi >= b.length()) return true;

  if (ai < a.length()) {
    int i = si;
    while (i < s.length()) {
      if (s[i] == a[ai]) {
        if (check(s,a,b,i+1,ai+1,bi)) {
          return true;
        }
      }
      ++i;
    }
  }

  if (bi < b.length()) {
    int i = si;
    while (i < s.length()) {
      if (s[i] == b[bi]) {
        if (check(s,a,b,i+1,ai,bi+1)) {
          return true;
        }
      }
      ++i;
    }
  }

  return false;
}

int main () {
  int T;
  string s,t,a,b;
  cin >> T;
  while (T--) {
    cin >> s >> t;
    bool possible = false;
    for (int i=0;i<t.length();++i) {
      a = t.substr(0,i);
      b = t.substr(i,t.length()-i);
      if (check(s, a, b, 0, 0, 0)) {
        possible = true;
        break;
      }
    }
    if (possible) {
      cout << "YES\n";
    }
    else {
      cout << "NO\n";
    }
  }

  return 0;
}
