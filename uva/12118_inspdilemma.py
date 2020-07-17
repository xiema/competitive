from sys import stdin,stdout

def dfs(g, u, p, f):
    e,o = 0,0
    f[u] = False
    for v in g[u]:
        if v == p:
            continue
        if v in f:
            if f[v]:
                continue
            else:
                e+=1
                continue
        _e,_o = dfs(g, v, u, f)
        e,o = e+_e+1,o+_o
    f[u] = True
    if len(g[u])%2:
        o += 1

    return e,o

I = 0
while True:
    V,E,T = map(int, stdin.readline().split())
    if V==0:
        break
    I+=1
    g = {u : set() for u in range(1,V+1)}
    for _ in range(E):
        a,b = map(int, stdin.readline().split())
        g[a].add(b)
        g[b].add(a)

    f = {}
    c,s = 0,0
    for i in range(1, V+1):
        if i in f:
            continue
        e,o = dfs(g, i, 0, f)
        c+=e
        if o > 2:
            c += (o-2)//2
        if e:
            s+=1
    if s:
        c+=s-1

    stdout.write('Case {}: {}\n'.format(I, c*T))
