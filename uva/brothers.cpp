#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

struct classcomp{
  bool operator()(const pii& a, const pii& b) const{
    return a.first < b.first || (a.first==b.first && a.second < b.second);
  }
};

int N,R,C,K;
map<pii, int, classcomp> *terr1, *terr2;
set<pii> *bord1, *bord2;

bool comphostile(int s1, int s2){
  return s2 == s1+1 || (s1==N-1 && s2==0);
}

void display(){
  int i=0;
  for (auto it=terr1->begin(); it!=terr1->end(); ++it){
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
  if (comphostile((*terr1)[coord1], (*terr1)[coord2])){
    (*terr2)[coord2] = (*terr1)[coord1];
    bord2->insert(coord2);
  }
}

void attack(const pii& coord){
  int i=coord.first, j=coord.second;
  if (i > 0) attack_aux(coord, pii(i-1,j));
  if (j > 0) attack_aux(coord, pii(i,j-1));
  if (i < R-1) attack_aux(coord, pii(i+1,j));
  if (j < C-1) attack_aux(coord, pii(i,j+1));
}



int main(){
  terr1 = new map<pii, int, classcomp>;
  terr2 = new map<pii, int, classcomp>;
  bord1 = new set<pii>;
  bord2 = new set<pii>;
  terr1->clear();
  terr2->clear();
  bord1->clear();
  bord2->clear();

  while (true){
    cin >> N >> R >> C >> K;
    if (N==0 && R==0 && C==0 && K==0) break;

    for (int i=0; i<R; ++i){
      for (int j=0; j<C; ++j){
        pii coord(i,j);
        cin >> (*terr1)[coord];
        (*terr2)[coord] = (*terr1)[coord];
        bord1->insert(coord);
      }
    }

    for (int bi=0; bi<K; ++bi){
      for (auto it=bord1->begin(); it!=bord1->end(); ++it){
        attack(*it);
      }
      bord1 = bord2;
      terr1 = terr2;
      bord2->clear();
    }

    display();
    terr1->clear();
    terr2->clear();
    bord1->clear();
  }
  return 0;
}
