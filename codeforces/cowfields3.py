from sys import stdin,stdout
from collections import deque
n,m,k = map(int,stdin.readline().split())
alist = list(map(int,stdin.readline().split()))
cnx = {}
for _ in range(m):
    x,y = map(int,stdin.readline().split())
    cnx.setdefault(x,[]).append(y)
    cnx.setdefault(y,[]).append(x)

next = deque([(1,0)])
scan = set(alist)
d1 = {}
while scan or n not in d1:
    v1,d = next.popleft()
    if v1 in d1:
        continue
    if v1 in scan:
        scan.remove(v1)
    d1[v1] = d
    for v2 in cnx[v1]:
        if v2 not in d1:
            next.append((v2,d+1))

next = deque([(n,0)])
scan = set(alist)
d2 = {}
while scan:
    v1,d = next.popleft()
    if v1 in d2:
        continue
    if v1 in scan:
        scan.remove(v1)
    d2[v1] = d
    for v2 in cnx[v1]:
        if v2 not in d2:
            next.append((v2,d+1))

alist.sort(key=lambda x: d1[x]-d2[x],reverse = True)
ans,hi = None,None
for a in alist:
    if hi==None:
        hi = d2[a]
        continue
    ans = d1[a]+hi if not ans else max(ans,d1[a]+hi)
    hi = max(hi, d2[a])

stdout.write(str(min(d1[n],ans+1)))
