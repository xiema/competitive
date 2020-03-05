#include <bits/stdc++.h>
using namespace std;

int main(){
  priority_queue<pair<int, int>, vector<pair<int,int> >, greater<pair<int, int> > > pq;
  map<int, int> m;
  string s;
  int id, period;
  while (true){
    cin >> s;
    if (s == "#") break;
    if (s == "Register"){
      cin >> id >> period;
      pq.emplace(period, id);
      m[id] = period;
    }
  }
  int c;
  pair<int, int> q;
  cin >> c;
  while (c--){
    q = pq.top();
    //cout << q.first << ' ' << q.second << '\n';
    cout << q.second << '\n';
    pq.emplace(q.first + m[q.second], q.second);
    pq.pop();
  }
  return 0;
}
