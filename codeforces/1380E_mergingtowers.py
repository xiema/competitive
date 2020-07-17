from sys import stdin,stdout
from collections import Counter

n,m = map(int, stdin.readline().split())
t = list(map(int, stdin.readline().split()))
L,R = {},{}
L[t[0]],R[t[0]] = set(),Counter()
C = 0
for i in range(1,n):
    if t[i] not in R:
        L[t[i]],R[t[i]] = set(),Counter()
    if t[i] != t[i-1]:
        R[t[i-1]][t[i]]+=1
        L[t[i]].add(t[i-1])
        C+=1

ans = [str(C)]

for _ in range(m-1):
    a,b = map(int, stdin.readline().split())
    for o in R[b]:
        if o == a:
            C-=R[b][a]
            R[b][o] = 0
        elif R[b][o]:
            R[a][o]+=R[b][o]
            L[o].add(a)
            R[b][o] = 0
    for o in L[b]:
        if o == a:
            C-=R[a][b]
            R[a][b] = 0
        elif R[o][b]:
            R[o][a] += R[o][b]
            R[o][b] = 0
            L[a].add(o)
    ans.append(str(C))

stdout.write('\n'.join(ans))
