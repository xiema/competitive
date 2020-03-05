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
while scan:
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

fdist = []
for a in order:
    next = deque([a])
    b = True
    while b:
        for _ in range(len(next)):
            v1 = next.popleft()
            if v1 in fpos:
                fdist.append((fpos[v1],dist[a]-dist[v1],a))
                b = False
            if b:
                lo = n
                for v2 in cnx[v1]:
                    lo = min(lo,dist[v2])
                for v2 in cnx[v1]:
                    if dist[v2] == lo:
                        next.append(v2)

#fdist.sort()
comp = set()
hi = -n
for f1 in fdist:
    rmv = set()
    add = True
    for f2 in comp:
        if f1[2]==f2[2]:
            continue
        d = f1[1]+f2[1]-(f1[0]-f2[0])
        hi = max(hi,d)
        d-=f1[1]
        if d <= f1[1]:
            rmv.add(f2)
        if d >= f1[1]:
            add = False
    comp -= rmv
    if add:
        comp.add(f1)

#print(short,hi)
stdout.write(str(min(0,hi+1)+dist[n]))
