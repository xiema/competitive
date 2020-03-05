#include <stdio.h>
int main()
{
  int count, num, temp;
  scanf("%d", &count);
  int fact[count];

  for (int i = 0; i < count; i++)
  {
    scanf("%d", &num);
    temp = num;
    for (int j = 2; j < num; j++)
    {
      temp *= j;
    }
    fact[i] = temp;
  }

  for (int i = 0; i < count; i++)
  {
    printf("%d\n", fact[i]);
  }

  return 0;
}
