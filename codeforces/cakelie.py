from sys import stdin, stdout
from collections import deque

t = int(stdin.readline().strip())
lines = []

for _ in range(t):
    n = int(stdin.readline().strip())
    verts = {}
    pieces = {}
    for i in range(1,n-2+1):
        a,b,c = stdin.readline().split()
        verts.setdefault(a, set()).add(i)
        verts.setdefault(b, set()).add(i)
        verts.setdefault(c, set()).add(i)
        pieces[i] = set([a,b,c])

    #print(verts)

    root,r1,r2,rootp = None, None, None, None
    for v,s in verts.items():
        if len(s) == 1:
            root = v
            rootp = s.copy().pop()
            rvs = pieces[rootp].copy()
            rvs.remove(root)
            r1 = rvs.pop()
            r2 = rvs.pop()
            break

    #print(pieces)
    stk = deque([(0, root), (1, rootp), (0, r2), (2, r1, r2, rootp), (0, r1)])

    vertord, pieceord = [], []
    while stk:
        cmd = stk.pop()
        t = cmd[0]
        if t == 0:
            vertord.append(cmd[1])
        elif t == 1:
            pieceord.append(cmd[1])
        else:
            _,v1,v2,p1 = cmd
            isect = verts[v1] & verts[v2]
            isect.remove(p1)
            if not isect:
                continue
            p2 = isect.pop()
            pvs = pieces[p2]
            pvs.remove(v1)
            pvs.remove(v2)
            v3 = pvs.pop()
            stk.append((1,p2))
            stk.append((2, v3,v2,p2))
            stk.append((0, v3))
            stk.append((2, v1,v3,p2))

    lines.append(' '.join(vertord) + '\n')
    lines.append(' '.join(map(str, pieceord)) + '\n')

stdout.writelines(lines)
