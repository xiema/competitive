#include <bits/stdc++.h>
using namespace std;

struct card {
  char face;
  char suit;

  card(char f, char s){
    face = f;
    suit = s;
  }

  bool operator == (card c){
    return (face == c.face || suit == c.suit);
  }
};

void display(list<stack<card>> &l){
  int sz = l.size();
  if (sz == 1){
    cout << sz << " pile remaining: ";
  } else {
    cout << sz << " piles remaining: ";
  }

  for (auto iter = l.begin(); iter != l.end(); ++iter){
    cout << iter->size() << " \n"[--sz==0];
  }
}

void move(stack<card> &s1, stack<card> &s2){
  //cout << s1.top().face << s1.top().suit << " over " << s2.top().face << s2.top().suit << " >>> ";
  s2.emplace(s1.top().face, s1.top().suit);
  s1.pop();
  //cout << s2.top().face << s2.top().suit << '\n';
}

int main(){
  char f,s;
  while (true){
    list<stack<card>> l;
    stack<card> *stk;

    for (int i=0; i<52; ++i){
      cin >> f >> s;
      if (f == '#') return 0;
      stk = new stack<card>;
      stk->emplace(f,s);
      l.push_back(*stk);
    }

    //display(l);

    int pos = 0;
    list<stack<card>>::iterator iter1 = l.begin(), iter2;
    while (iter1 != l.end()){
      //display(l);
      //cout << pos << ' ' << iter1->top().face << iter1->top().suit << '\n';
      //cout << pos << ' ' << l.size() << '\n';
      if (pos >= 3){
        iter2 = prev(iter1,3);
        if (iter1->top() == iter2->top()){
          move(*iter1, *iter2);
          //cout << s2.top().face << s2.top().suit << '\n';
          if (iter1->empty()){
            iter1 = l.erase(iter1);
          }
          pos-=3;
          iter1 = prev(iter1,3);
          //cout << iter1->top().face << iter1->top().suit << '\n';
          continue;
        }
      }

      if (pos >= 1){
        iter2 = prev(iter1,1);
        if (iter1->top() == iter2->top()){
          move(*iter1, *iter2);
          //cout << s2.top().face << s2.top().suit << '\n';
          if (iter1->empty()){
            iter1 = l.erase(iter1);
          }
          --pos;
          --iter1;
          //cout << iter1->top().face << iter1->top().suit << '\n';
          continue;
        }
      }

      ++pos;
      ++iter1;
    }

    display(l);
  }

  return 0;
}
