#include <iostream>
#include <string>
using namespace std;

void inc(string& num, int i) {
  if (num[i] == '9'){
    num[i] = '0';
    if (i > 0) inc(num, i-1);
  } else {
    ++num[i];
  }
}

int main(){
  int T;
  cin >> T;

  string num, out;
  while (T-- > 0){
    cin >> num;
    int l = num.length();

    int left=0, right=l-1;
    inc(num, right);
    //check 00000...
    if (num[left] == '0'){
      num[right] = '1';
      out = out + '1' + num + '\n';
      continue;
    }
    while (left < right){
      if (num[left] > num[right]) {
        num[right] = num[left];
      } else if (num[right] > num[left]) {
        inc(num, right-1);
        num[right] = num[left];
      }
      ++left;
      --right;
    }

    out = out + num + '\n';
  }

  cout << out;
  return 0;
}
