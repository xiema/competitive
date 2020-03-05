#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

struct classcomp{
  bool operator()(const pii& a, const pii& b) const{
    return a.first < b.first || (a.first==b.first && a.second < b.second);
  }
};

int N,R,C,K;
map<pii, int, classcomp> terr1, terr2;
//set<pii> bord1, bord2;
list<pii> bord1;
map<pii, list<pii>> adj;

bool comphostile(int s1, int s2){
  return s2 == (s1+1)%N ;
}

void getadj(pii coord){
  if (adj.find(coord)==adj.end()){
    int i=coord.first, j=coord.second;
    adj[coord].push_back(pii(i+1,j));
    adj[coord].push_back(pii(i,j+1));
  }
}

void display(){
  int i=0;
  for (auto it=terr1.begin(); it!=terr1.end(); ++it){
    cout << it->second;
    if (++i == C){
      i=0;
      cout << '\n';
    } else {
      cout << ' ';
    }
  }
}

void attack_aux(const pii& coord1, const pii& coord2){
  if (terr1.find(coord2)!=terr1.end()){
    int s1 = terr1[coord1], s2 = terr1[coord2];
    if (comphostile(s1,s2)){
      terr2[coord2] = s1;
      //bord2.insert(coord2);
    } else if (comphostile(s2,s1)){
      terr2[coord1] = s2;
      //bord2.insert(coord1);
    }
  }
}

void attack(const pii& coord){
  for (auto it=adj[coord].begin(); it!=adj[coord].end(); ++it){
    attack_aux(coord, *it);
  }
}



int main(){
  while (true){
    cin >> N >> R >> C >> K;
    if (N==0 && R==0 && C==0 && K==0) break;

    for (int i=0; i<R; ++i){
      for (int j=0; j<C; ++j){
        pii coord(i,j);
        cin >> terr1[coord];
        terr2[coord] = terr1[coord];
        bord1.push_back(coord);
        getadj(coord);
      }
    }

    for (int bi=0; bi<K; ++bi){
      //cout << bord1.size() << '\n';
      /*
      for (auto it=bord1.begin(); it!=bord1.end(); ++it){
        attack(*it);
      }
      */
      for (auto it=bord1.begin(); it!=bord1.end(); ++it){
        attack(*it);
      }
      //bord1 = bord2;
      terr1 = terr2;
      //bord2.clear();
      //display();
    }

    display();
    //terr1.clear();
    //terr2.clear();
    bord1.clear();
    adj.clear();
  }
  return 0;
}
