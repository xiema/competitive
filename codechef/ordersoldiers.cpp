#include <iostream>
#include <list>
#include <string>
using namespace std;

int s[200000];

int main(){
  int T,n,i,j,v,temp;
  cin >> T;

  while (T-- > 0){
    cin >> n;
    for (i=0; i<n; ++i){
      cin >> s[i];
    }

    string out;
    list<int> bar_extent;
    for (i=n-1; i>=0; --i){
      v = i+1-s[i];
      if (!bar_extent.empty()){
        v += bar_extent.size();
        if (bar_extent.front() >= i){
          bar_extent.pop_front();
        }
      }
      if (s[i]) {
        temp = i-s[i];
        list<int>::iterator iter = bar_extent.begin();
        while (iter != bar_extent.end()){
          if (*iter <= temp) {
            break;
          }
          ++iter;
        }
        bar_extent.insert(iter, temp);
      }
      out = to_string(v) + ' ' + out;
    }

    cout << out << '\n';
  }

  return 0;
}
