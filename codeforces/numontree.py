from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
verts = {}
counts = {}
sub = {}
root = None
for i in range(1,n+1):
    p,c = map(int, stdin.readline().split())
    if not p:
        root = i
    else:
        verts.setdefault(p,set()).add(i)
        counts[i] = c


next = deque([root])
sub[root] = set(counts.keys())
sub[root].remove(root)
while next:
    v1 = next.popleft()
    cur = sub[v1] - verts[v1]
    for v2 in verts[v1]:
        next.append(v2)
        sub[v2] = cur.copy()
