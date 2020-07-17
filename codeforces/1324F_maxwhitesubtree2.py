from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().split()))

t = {}
for _ in range(n-1):
    u,v = map(int,stdin.readline().split())
    t.setdefault(u, set()).add(v)
    t.setdefault(v, set()).add(u)

M = {}

def dfs_dn(r):
    stk = deque([(0, r)])
    s = set()
    while stk:
        f,u = stk.pop()
        if f:
            M[u] = 1 if a[u-1] else -1
            for v in t[u]:
                if v in M and M[v] > 0:
                    M[u] += M[v]
            continue
        stk.append((1, u))
        s.add(u)
        for v in t[u]:
            if v in s:
                continue
            stk.append((0, v))

def dfs_up(r):
    stk = deque([(r, 0)])
    s = set()
    while stk:
        u,m = stk.pop()
        if m > 0:
            M[u] += m
        s.add(u)
        for v in t[u]:
            if v in s:
                continue
            if M[v] > 0:
                stk.append((v, M[u]-M[v]))
            else:
                stk.append((v, M[u]))

dfs_dn(1)
dfs_up(1)

print(' '.join([str(M[i]) for i in range(1,n+1)]))
