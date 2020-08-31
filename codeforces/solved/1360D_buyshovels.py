from sys import stdin,stdout
from math import sqrt,floor

t = int(stdin.readline().strip())
for _ in range(t):
    n,k = map(int,stdin.readline().split())
    l = floor(sqrt(n))+1
    ans = None
    i = 1
    while i<l:
        if i>k:
            if ans:
                ans = n//ans
            break
        if n%i==0:
            ans = i
            if n//i<=k:
                break
        i+=1
    else:
        if ans:
            ans = n//ans
        else:
            ans = n

    stdout.write('{}\n'.format(ans))
