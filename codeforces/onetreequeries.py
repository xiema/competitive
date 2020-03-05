from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
cnx = {}
for _ in range(n-1):
    u,v = map(int,stdin.readline().split())
    cnx.setdefault(u,[]).append(v)
    cnx.setdefault(v,[]).append(u)

depth,idx1,idx2 = {},{},{}
nearest = {}
vert = [False for _ in range(n+1)]
vert[1] = True
idx = 0
next = deque([(1,1,0,True)])
while next:
    v1,p,d,b = next.pop()
    if not b:
        idx2[v1],idx = idx,idx+1
        continue
    depth[v1] = d
    idx1[v1],idx = idx,idx+1
    next.append((v1,p,d,False))
    cnt = 0
    for v2 in cnx[v1]:
        if v2!=p:
            next.append((v2,v1,d+1,True))
            cnt+=1
    if vert[p]:
        nearest[v1] = p
    else:
        nearest[v1] = nearest[p]
    if cnt > 1:
        vert[v1] = True


def lca(a,b):
    while True:
        if idx1[a]<=idx1[b] and idx2[a]>=idx2[b]:
            return a
        if idx1[a]>=idx1[b] and idx2[a]<=idx2[b]:
            return b
        a = nearest[a]

def get_path(s,e):
    v = lca(s,e)
    return abs(depth[s]-depth[v]) + abs(depth[e]-depth[v])

q = int(stdin.readline().strip())
out = []
for _ in range(q):
    x,y,a,b,k = map(int,stdin.readline().split())
    d1 = get_path(a,b)
    if d1 <= k and d1%2 == k%2:
        out.append("YES\n")
        continue
    d2 = min(get_path(a,x)+get_path(b,y),get_path(a,y)+get_path(b,x))+1
    if d2 <= k and d2%2 == k%2:
        out.append("YES\n")
        continue
    out.append("NO\n")

stdout.writelines(out)
