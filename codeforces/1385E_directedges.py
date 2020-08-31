from sys import stdin,stdout
from collections import deque

def dfs(r,G,E,R,F):
    stk = deque([(0,r,0,None)])
    while stk:
        f,u,p,e = stk.pop()
        if f==2:
            F[u] = True
            continue
        if f==1:
            if u in E:
                for v in E[u]:
                    if v == p:
                        continue
                    if v in F:
                        if not F[v]:
                            R[(u,v)] = False
                        continue
                    R[(u,v)] = True
                    stk.append((0,v,u,(u,v)))
            stk.append((2,u,p,None))
            continue
        if u in F:
            continue
        F[u] = False
        stk.append((1,u,p,None))
        if u in G:
            for v in G[u]:
                if v in F:
                    if F[v]:
                        continue
                    elif e:
                        R[e] = False
                    else:
                        return False
                stk.append((0,v,u,e))

    return True




t = int(stdin.readline().strip())
for _ in range(t):
    n,m = map(int, stdin.readline().split())
    G,E = {},{}
    for _ in range(m):
        t,x,y = map(int, stdin.readline().split())
        if t:
            G.setdefault(x, set()).add(y)
        else:
            E.setdefault(x, set()).add(y)
            E.setdefault(y, set()).add(x)

    R,F = {},{}
    for r in range(1,n+1):
        if r in F:
            continue
        if not dfs(r,G,E,R,F):
            stdout.write("NO\n")
            break
    else:
        print(R)
        stdout.write("YES\n")
        for (u,v),d in R.items():
            if d:
                stdout.write('{} {}\n'.format(u,v))
            else:
                stdout.write('{} {}\n'.format(v,u))

        for u,vs in G.items():
            for v in vs:
                stdout.write('{} {}\n'.format(u,v))
