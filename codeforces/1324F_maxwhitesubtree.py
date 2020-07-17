from sys import stdin

n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().split()))

t = {}
for _ in range(n-1):
    u,v = map(int,stdin.readline().split())
    t.setdefault(u, set()).add(v)
    t.setdefault(v, set()).add(u)

M = {}

def dfs_dn(u, s):
    s.add(u)
    m = 1 if a[u-1] else -1
    for v in t[u]:
        if v in s:
            continue
        dfs_dn(v, s)
        if M[v] > 0:
            m += M[v]
    M[u] = m

def dfs_up(u, s, m):
    if m > 0:
        M[u] += m
    s.add(u)
    for v in t[u]:
        if v in s:
            continue
        if M[v] > 0:
            dfs_up(v, s, M[u]-M[v])
        else:
            dfs_up(v, s, M[u])

dfs_dn(1, set())
dfs_up(1, set(), 0)

print(' '.join([str(M[i]) for i in range(1,n+1)]))
