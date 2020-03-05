#include <bits/stdc++.h>
using namespace std;

struct P{
  string name;
  int d,m,y;

/*
  bool operator<(const P& a) const {
    if (y < a.y){
      return true;
    } else if (y == a.y){
      if (m < a.m) {
        return true;
      } else if (m == a.m && d < a.d){
        return true;
      }
    }
    return false;
  }
*/
};

bool comp(P& a, P& b){
  if (a.y < b.y){
    return true;
  } else if (a.y == b.y){
    if (a.m < b.m) {
      return true;
    } else if (a.m == b.m && a.d < b.d){
      return true;
    }
  }
  return false;
}

int main(){
  int c;
  cin >> c;
  P v[c];
  for (int i=0; i<c; ++i){
    cin >> v[i].name >> v[i].d >> v[i].m >> v[i].y;
  }
  sort(v, v+c, comp);

  for (int i=0; i<c; ++i){
    cout << v[i].name << '\n';
  }

  cout << v[c-1].name << '\n' << v[0].name;

  return 0;
}
