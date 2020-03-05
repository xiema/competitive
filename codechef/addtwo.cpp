#include <stdio.h>
int main()
{
  int count;
  scanf("%d", &count);
  int a, b, sum[count];

  for (int i = 0; i < count; i++)
  {
    scanf("%d %d", &a, &b);
    sum[i] = a + b;
  }

  for (int i = 0; i < count; i++)
  {
    printf("%d\n", sum[i]);
  }

  return 0;
}

int main() {
  
  
  return 0;
}