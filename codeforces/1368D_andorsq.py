from sys import stdin
from collections import Counter


n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))

c,m = Counter(),0
for a in alist:
    i = 0
    while a:
        if a%2:
            c[i]+=1
        a//=2
        i+=1
    m = max(m,i)

p = {}
e = 1
for i in range(m):
    p[i] = e
    e *= 2

ans = 0
while True:
    b = 0
    for i in c:
        if c[i] > 0:
            b += p[i]
            c[i]-=1
    if b:
        ans += b*b
    else:
        break

print(ans)
