from sys import stdin
from collections import deque

n = int(stdin.readline().strip())

verts = {}
for _ in range(n-1):
    v1,v2 = map(int, stdin.readline().split())
    verts.setdefault(v1, set()).add(v2)
    verts.setdefault(v2, set()).add(v1)

root = None
for v,k in verts.items():
    if len(k) == 1:
        root = v
        break

def longest_path_aux(verts, root):
    r,l = None,0
    seen = set()
    next = deque([[root]])
    while next:
        path = next.popleft()
        v1 = path[-1]
        seen.add(v1)
        end = True
        for v2 in filter(lambda x: x not in seen, verts[v1]):
            next.append(path + [v2])
            end = False
        if end and len(path) > l:
            r,l = path,len(path)
    return r

def longest_path(verts, root, prev = None):
    path = longest_path_aux(verts, root)
    if prev and prev == path[-1]:
        return path
    else:
        return longest_path(verts, path[-1], root)

path = longest_path(verts, root)
print(path)
k,S = 0,0
for v in path:
    S += (len(verts[v])-1) * k
    k+=1
else:
    S += (k-1)
print(S)
