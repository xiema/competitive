#include <unordered_set>
#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;

void match(string &s1, string &s2, string &out) {
  int l = s1.length();
  char c;
  for (int i=0;i<l;++i) {
    if (s1[i] == s2[i]) {
      c = s1[i];
    }
    else {
      switch (s1[i]) {
        case 'S':
          c = s2[i]=='T' ? 'E' : 'T';
          break;
        case 'E':
          c = s2[i]=='T' ? 'S' : 'T';
          break;
        case 'T':
          c = s2[i]=='E' ? 'S' : 'E';
          break;
      }
    }
    out[i] = c;
  }
}

int main() {
  int n,k;
  cin >> n >> k;
  unordered_map<string, int> s2i;
  vector<string> i2s(n);
  vector<unordered_set<int> > cnx(n);

  string s;
  for (int i=0;i<n;++i) {
    cin >> s;
    s2i[s] = i, i2s[i] = s;
    cnx[i].clear();
  }

  int c = 0;
  for (int i=0;i<n;++i) {
    for (int j=i+1;j<n;++j) {
      if (cnx[i].find(j)!=cnx[i].end()) continue;

      match(i2s[i],i2s[j],s);
      auto x = s2i.find(s);
      if (x!=s2i.end()) {
        cnx[i].emplace(x->second);
        cnx[j].emplace(x->second);
        ++c;
      }
    }
  }

  cout << c;

  return 0;
}
