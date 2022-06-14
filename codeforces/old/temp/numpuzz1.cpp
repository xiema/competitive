#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  string s;
  vector<int> cnt;
  for (int i='a'; i<='i'; ++i) {
    cnt.push_back(0);
  }
  int i = 0;
  while(getline(cin, s)) {
    ++i;
    for (auto it=s.begin(); it!=s.end(); ++it) {
      cnt[*it-'a'] += 1;
    }

    cout << "Case #" << i << ":\n";

    cout << (cnt['a'-'a'] + cnt['b'-'a'] + cnt['d'-'a'])%10 << ' ';
    cout << (cnt['a'-'a'] + cnt['b'-'a'] + cnt['c'-'a'] + cnt['e'-'a'])%10 << ' ';
    cout << (cnt['b'-'a'] + cnt['c'-'a'] + cnt['f'-'a'])%10 << '\n';

    cout << (cnt['a'-'a'] + cnt['d'-'a'] + cnt['e'-'a'] + cnt['g'-'a'])%10 << ' ';
    cout << (cnt['b'-'a'] + cnt['d'-'a'] + cnt['e'-'a'] + cnt['f'-'a'] + cnt['h'-'a'])%10 << ' ';
    cout << (cnt['c'-'a'] + cnt['e'-'a'] + cnt['f'-'a'] + cnt['i'-'a'])%10 << '\n';

    cout << (cnt['d'-'a'] + cnt['g'-'a'] + cnt['h'-'a'])%10 << ' ';
    cout << (cnt['e'-'a'] + cnt['g'-'a'] + cnt['h'-'a'] + cnt['i'-'a'])%10 << ' ';
    cout << (cnt['f'-'a'] + cnt['h'-'a'] + cnt['i'-'a'])%10 << '\n';

    for (auto it=cnt.begin(); it!=cnt.end(); ++it) {
      *it = 0;
    }
  }
  return 0;
}
