#include <bits/stdc++.h>
using namespace std;

int main(){
  int T,n,myjob,j;
  cin >> T;
  while (T-- > 0){
    deque<int> dq;
    priority_queue<int> pq;
    cin >> n >> myjob;
    while (n-- > 0){
      cin >> j;
      dq.push_back(j);
      pq.push(j);
    }

    int time=0;
    while (true){
      if (myjob == 0){
        if (dq.front() == pq.top()){
          ++time;
          break;
        } else {
          myjob = dq.size();
          dq.push_back(dq.front());
        }
      } else {
        if (dq.front() == pq.top()){
          ++time;
          pq.pop();
        } else {
          dq.push_back(dq.front());
        }
      }
      dq.pop_front();
      --myjob;
    }

    cout << time << '\n';
  }

  return 0;
}
