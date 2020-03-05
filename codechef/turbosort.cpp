#include <stdio.h>
#include <stdlib.h>

void insert(int* num, int end, int n) {
  if (end == 0) {
    num[0] = n;
    return;
  } else {
    int pos = end;
    while (pos > 0 && num[pos-1] > n) {
      num[pos] = num[pos-1];
      --pos;
    }
    num[pos] = n;
  }
}

int main()
{
  int count;
  scanf("%d", &count);
  int num[count];

  for (int i = 0; i < count; ++i) {
    int n;
    scanf("%d", &n);
    insert(num, i, n);
  }

  for (int i=0; i < count; ++i) {
    printf("%d\n", num[i]);
  }
  return 0;
}
