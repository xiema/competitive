from sys import stdin,stdout
from collections import Counter

Pr = []
Cm = set()
for i in range(2,450):
    if i in Cm:
        continue
    Pr.append(i)
    for j in range(i,450,i):
        Cm.add(j)

n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))

D = {}
for a in alist:
    for p in Pr:
        if a==1 or a%p:
            continue
        if p not in D:
            D[p] = Counter()
        i=1
        while a%p==0:
            D[p][i]+=1
            a//=p
            i+=1
    if a > 1:
        if a not in D:
            D[a] = Counter()
        D[a][1]+=1
ans = 1
for p,c in D.items():
    x = 0
    for i,v in c.items():
        if v==n or v==n-1:
            x=max(x,i)
    ans*=p**x

print(ans)
