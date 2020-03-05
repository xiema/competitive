#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t){
    int CF;
    cin >> CF;
    set<int> unique_stamps;
    set<int> nonunique_stamps;
    map<int,int> stamp_owners;
    vector<int> unique_count(CF+1);
    for (int i=1; i<=CF; ++i){
      int CS;
      cin >> CS;
      while (CS--){
        int n;
        cin >> n;
        if (nonunique_stamps.find(n) == nonunique_stamps.end()){
          if (stamp_owners[n] != i){
            if (unique_stamps.find(n) == unique_stamps.end()){
              stamp_owners[n] = i;
              ++unique_count[i];
              unique_stamps.insert(n);
            } else {
              unique_stamps.erase(n);
              --unique_count[stamp_owners[n]];
              nonunique_stamps.insert(n);
            }
          }
        }
      }
    }
    double total = unique_stamps.size();
    printf("Case %d: ", t);
    for (int i=1; i<=CF; ++i){
      printf("%f%%", ((double)unique_count[i])*100/total);
      cout << " \n"[i==CF];
    }
  }
  return 0;
}
