#include <iostream>
#include <vector>
using namespace std;

bool coins[100000];

void _ins(int pos[], int& sz, int& i, int N){
  while (i < sz){
    if (pos[i] == N){
      return;
    } else if (pos[i] > N){
      for (int j=sz; j>i; --j){
        pos[j] = pos[j-1];
      }
      pos[i] = N;
      ++sz;
      return;
    }
    ++i;
  }

  pos[i] = N;
  ++sz;
}

void insert(int pos[], int& sz, int A, int B){
  int i = 0;

  _ins(pos, sz, i, A);
  _ins(pos, sz, i, B);
}

void p(bool b, int pos[], int sz){
  cout << "* ";
  if (b){
    cout << "head ";
  } else {
    cout << "tail ";
  }
  for (int i=0; i<sz; ++i){
    cout << pos[i] << ' ';
  }
  cout << '\n';
}

int main(){
  int N, Q, count, C,A,B;
  cin >> N >> Q;
  int pos[100000] = {0, N};
  bool b = false;
  int sz = 2;
  while (Q-- > 0){
    cin >> C >> A >> B;
    ++B;
    if (C){
      count = 0;
      int i;
      if (b)
        i=0;
      else
        i=1;
      while (i < sz-1){
        int j = i+1;
        if (A < pos[j] && B > pos[i]){
          count += (min(B, pos[j]) - max(A, pos[i]));
        }
        i+=2;
      }
      cout << count << '\n';
    } else {
      insert(pos, sz, A, B);
      if (A == 0) b = !b;
      p(b, pos, sz);
    }
  }
  return 0;
}
