#include <iostream>
using namespace std;

struct Node{
  int pos, dif;
  Node *left, *right;
};

Node* newnode(int pos){
  Node* n = new Node;
  n->pos = pos;
  n->left = n->right = NULL;
  n->dif = 1;
  return n;
}

Node* ins(Node* parent, int i, int v){
  if (parent == NULL){
    return newnode(i);
  }
  if (v >= parent->dif){
    parent->left = ins(parent->left, i, v-parent->dif);
  } else {
    parent->right = ins(parent->right, i, v);
    parent->dif++;
  }

  return parent;
}

void extract(Node* n, int s[], int& start){
  if(n == NULL) return;
  extract(n->left, s, start);
  s[n->pos] = ++start;
  extract(n->right, s, start);

  delete n;
}

int main(){
  int T,n,i,v,s[200000];
  Node* tree;
  cin >> T;

  while (T--){
    cin >> n;

    tree = NULL;
    for (i=0; i<n; ++i){
      cin >> v;
      tree = ins(tree, i, v);
    }

    int start = 0;
    extract(tree, s, start);
    for (i=0; i<n; ++i){
      cout << s[i] << ' ';
    }

    cout << '\n';
  }
  return 0;
}
