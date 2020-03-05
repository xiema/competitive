#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int count;
  scanf("%d", &count);
  vector<int> num;

  for (int i = 0; i < count; ++i) {
    int n;
    scanf("%d", &n);
    num.push_back(n);
  }

  sort(num.begin(), num.end());
  for (int i=0; i < count; ++i) {
    printf("%d\n", num[i]);
  }
  return 0;
}
