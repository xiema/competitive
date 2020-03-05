#include <iostream>
using namespace std;

int f(int n){
  if (n != 0) {
    return max(n, f(n/2)+f(n/3)+f(n/4));
  } else {
    return n;
  }
}

int main(){
  int n;

  while (true){
    cin >> n;
    cout << f(n) << '\n';
  }

  return 0;
}
