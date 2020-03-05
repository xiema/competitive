#include <iostream>
#include <cmath>
using namespace std;

int N, *tree, *num, *func;

int get_mid(int begin, int end){ return begin + (end-begin)/2; }

int sum(int begin, int end, int cur, int qbegin, int qend){
  if (qbegin <= begin && qend >= end) return tree[cur];

  if (qend < begin || qbegin > end) return 0;

  int mid = get_mid(begin, end);
  return sum(begin, mid, 2*cur+1, qbegin, qend) + sum(mid+1, end, 2*cur+2, qbegin, qend);
}

int fsum(int begin, int end){
  int res = 0;
  int i=begin*2;
  int j=i+1;
  while (i <= end*2) {
    int s = sum(0, N-1, 0, func[i], func[j]);
    res += s;
    i+=2; j+=2;
  }
  return res;
}

void update_util(int begin, int end, int cur, int i, int dif){
  if (i < begin || i > end) return;

  tree[cur] += dif;
  if (begin != end){
    int mid = get_mid(begin, end);
    update_util(begin, mid, 2*cur+1, i, dif);
    update_util(mid+1, end, 2*cur+2, i, dif);
  }
}

void update(int i, int v){
  int dif = v - num[i];
  num[i] = v;
  update_util(0, N-1, 0, i, dif);
}

int make_tree(int begin, int end, int cur){
  if (begin == end){
    tree[cur] = num[begin];
  } else {
    int mid = get_mid(begin, end);
    tree[cur] = make_tree(begin, mid, cur*2+1) + make_tree(mid+1, end, cur*2+2);
  }
  return tree[cur];
}

int main(){
  cin >> N;
  num = new int[N];
  func = new int[N*2];

  for (int i=0; i<N; ++i){
    cin >> num[i];
  }
  return 0;

  int treesz = 4*N;
  tree = new int[treesz];
  make_tree(0,N-1,0);

  cout << treesz << '\n';
  for (int i=0; i<treesz; ++i){
    cout << tree[i] << ' ';
  }
  cout << '\n';

  for (int i=0; i<N*2; ++i){
    cin >> func[i];
    --func[i];
  }


  int Q, type, a, b;
  cin >> Q;
  while (Q--){
    cin >> type >> a >> b;
    if (type == 2) {
      cout << fsum(a-1, b-1) << '\n';
    } else {
      update(a-1, b);
    }
  }


  return 0;
}
