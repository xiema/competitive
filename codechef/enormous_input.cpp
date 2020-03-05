#include <stdio.h>
int main()
{
  int count;
  long divisor;
  scanf("%d %d", &count, &divisor);
  int result = 0;

  for (int i = 0; i < count; i++)
  {
    long num;
    scanf("%d", &num);
    if (num % divisor == 0)
    {
      result++;
    }
  }

  printf("%d", result);

  return 0;
}
