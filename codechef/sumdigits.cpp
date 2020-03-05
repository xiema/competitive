#include <stdio.h>
#include <stdlib.h>
int main()
{
  int count, temp=0, d, c=0;
  char digit;
  scanf("%d\n", &count);
  int sum[count];

  while (c < count)
  {
    digit = getchar();
    if (digit == '\n')
    {
      sum[c] = temp;
      temp = 0;
      c++;
    } else
    {
      temp += int(digit)-48;
    }
  }

  for (int i = 0; i < count; i++)
  {
    printf("%d\n", sum[i]);
  }

  return 0;
}
