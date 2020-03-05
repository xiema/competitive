#include <bits/stdc++.h>
using namespace std;

struct node{
  int mostfrequent, start, end, mid;
  node *left, *right;
};

node* createnode(vector<pair<int,int> > &v, int start, int end, int &idx){
  node* n = new node;
  if (start == end){
    n->mostfrequent = v[start].second;
    n->start = idx;
    n->end = (idx += n->mostfrequent)-1;
    n->left = n->right = NULL;

  } else {
    n->start = idx;
    int mid = (start+end)/2;
    n->left = createnode(v, start, mid, idx);
    n->mid = idx-1;
    n->right = createnode(v, mid+1, end, idx);
    n->mostfrequent = max(n->left->mostfrequent, n->right->mostfrequent);
    n->end = idx-1;
  }

  return n;
}

int getmostfrequent(node *n, int start, int end){
  //printf("gmf %d %d - %d %d\n", start, end, n->start, n->end);
  //out of range
  if (start > n->end || end < n->start) return 0;

  //node/leaf, full
  if (start == n->start && end == n->end){
    return n->mostfrequent;
  }

  //leaf, partial
  if (n->left == NULL){
    return min(end,n->end) - max(start,n->start) + 1;
  }

  //node, partial
  return max(getmostfrequent(n->left, start, min(end, n->left->end)), getmostfrequent(n->right, max(start, n->right->start), end));
}

int main(){
  while (true){
    int n,q;
    cin >> n >> q;
    if (n==0) break;
    vector<pair<int,int> > v;

    int num;
    cin >> num;
    int curnum = num, count = 1;
    for (int i=1; i<n; ++i){
      cin >> num;
      if (num == curnum){
        ++count;
      } else {
        v.emplace_back(curnum, count);
        curnum = num;
        count = 1;
      }
    }
    v.emplace_back(curnum, count);

    /*
    for (auto it=v.begin(); it!=v.end(); ++it){
      printf("%d %d\n", it->first, it->second);
    }
    */

    int idx = 1;
    node* tree = createnode(v, 0, v.size()-1, idx);

    for (int i=0; i<q; ++i){
      int a,b;
      cin >> a >> b;
      cout << getmostfrequent(tree, a, b) << '\n';
    }
  }
  return 0;
}
