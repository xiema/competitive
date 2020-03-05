#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

struct P{
  string name;
  int d,m,y;
};

bool comp(const P& a, const P& b){
  if (a.y < b.y)
    return true;
  if (a.y == b.y && a.m < b.m)
    return true;
  if (a.y == b.y && a.m == b.m && a.d < b.d)
    return true;

  return false;
}

void display(P v[], int n){
  for (int i=0; i<n; ++i){
    cout << v[i].name << ' ' << v[i].y << ' ' << v[i].m << ' ' << v[i].d << '\n';
  }
}

int main(){
  int c,d,m,y;
  string name;
  cin >> c;
  P v[c];
  for (int i=0; i<c; ++i){
    cin >> name >> d >> m >> y;
    v[i].name = name;
    v[i].d = d;
    v[i].m = m;
    v[i].y = y;
  }
  sort(v, v+c, comp);
  display(v, c);

  cout << v[c-1].name << '\n' << v[0].name;

  return 0;
}
