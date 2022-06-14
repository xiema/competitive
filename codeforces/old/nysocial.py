from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())

treea,treeb = {},{}
for _ in range(n-1):
    a,b = stdin.readline().split()
    treea.setdefault(a, set()).add(b)
    treea.setdefault(b, set()).add(a)

for _ in range(n-1):
    a,b = stdin.readline().split()
    treeb.setdefault(a, set()).add(b)
    treeb.setdefault(b, set()).add(a)

root,rootc = None,None
for v,vs in treea.items():
    if len(vs) == 1:
        root = v
        for vv in vs:
            rootc = vv
        break

ordered = deque()
next = deque([(rootc, root)])
repl = {root: set()}
sub = {root: set([root])}
while next:
    v1,p = next.popleft()
    if v1 in sub:
        continue
    ordered.appendleft((v1,p))
    sub[v1] = set([v1])
    repl[v1] = set()
    for v2 in treea[v1]:
        if v2 != p:
            next.append((v2, v1))

print(treea)
print(treeb)
for v1,v2 in ordered:
    repl[v1].update(treeb[v1])
    repl[v1] -= sub[v1]
    edg = "{} {} ".format(v1,v2)
    for a in repl[v1]:
        for b in filter(lambda x: x in sub[v1], treeb[a]):
            stdout.write(edg)
            stdout.write("{} {}\n".format(a,b))
    repl[v2].update(repl[v1])
    sub[v2].update(sub[v1])
