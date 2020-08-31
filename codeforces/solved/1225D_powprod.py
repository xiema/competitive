from sys import stdin
from math import pow
from collections import Counter

n,k = map(int ,stdin.readline().split())
alist = list(map(int, stdin.readline().split()))
c = Counter()
for a in alist:
    c[a]+=1

p = {}
i=2
while True:
    y = pow(i,k)
    if y > 100000:
        break
    x,y = i,
    if i not in p:
        j,x = 1,i
        while j < k:
            p[x] = (i, j)
            x*=i
            j+=1
    i+=1

c = Counter()
for a in alist:
    if a == 1:
        c[1]+=1
        continue
    if a in pow:
        c[pow[a]]+=1
