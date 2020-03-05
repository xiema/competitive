#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;

int main()
{
  int count;
  string out;
  scanf("%d", &count);
  for (int i=0; i<count; ++i) {
    int a, b;
    scanf("%d %d", &a, &b);
    out = out + to_string(a%b) + "\n";
  }

  cout << out;
  return 0;
}
