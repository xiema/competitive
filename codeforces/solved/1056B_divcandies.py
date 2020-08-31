from sys import stdin
from collections import Counter

n,m = map(int, stdin.readline().split())
Ca,Cb = Counter(),Counter()

r = n%m
for i in range(1,m+1):
    x = ((i%m)*(i%m))%m
    if i<=r:
        Cb[x]+=1
    Ca[x]+=1

d = n//m
for c in Ca:
    Ca[c] = Ca[c]*d + Cb[c]

C = 0
for i in range(m//2+1):
    if Ca[i]:
        j = (m-i)%m
        if i==j:
            C+=Ca[i]*Ca[i]
        else:
            C+=Ca[i]*Ca[j]*2

print(C)
