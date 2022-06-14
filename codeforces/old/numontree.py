from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
verts = {}
children = {}
for i in range(1,n+1):
    p,c = map(int, stdin.readline().split())
    children.setdefault(p,set()).add(i)
    verts[i] = (p,c)

root = children[0].pop()
ordered = deque()
next = deque([root])
while next:
    v1 = next.popleft()
    ordered.appendleft(v1)
    if v1 in children:
        for v2 in children[v1]:
            next.append(v2)
inc = []
possible = True
for v1 in ordered:
    v2,c = verts[v1]
    if c > len(inc):
        possible = False
        break
    inc.insert(c,v1)

if not possible:
    stdout.write("NO")
else:
    vals = [0 for i in range(n+1)]
    i=1
    for v in inc:
        vals[v] = i
        i+=1
    stdout.write("YES\n")
    stdout.write(' '.join(map(str, vals[1:])))
