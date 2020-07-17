from sys import stdin
from collections import namedtuple,deque

Node = namedtuple('Node', ['a','b','c'])

n = int(stdin.readline().strip())

N = {}
for i in range(1,n+1):
    N[i] = Node(*map(int, stdin.readline().split()))

T = {}
T[1] = set()
for _ in range(n-1):
    u,v = map(int, stdin.readline().split())
    T.setdefault(u, set()).add(v)
    T.setdefault(v, set()).add(u)

q = deque([(0, 1, 0, N[1].a)])
R = {}
M = 0
while q:
    f,u,p,m = q.pop()
    if f==0:
        R[u] = [0,0]
        m = min(m, N[u].a)
        q.append((1, u, p, m))
        for v in T[u]:
            if v == p:
                continue
            q.append((0, v, u, m))
    else:
        if N[u].b != N[u].c:
            R[u][N[u].c]+=1
        if R[u][0] and R[u][1]:
            d = min(R[u][0],R[u][1])
            R[u][0],R[u][1] = R[u][0]-d,R[u][1]-d
            M += d*2*m
        if p != 0:
            R[p][0]+=R[u][0]
            R[p][1]+=R[u][1]
if R[1][0] or R[1][1]:
    M = -1

print(M)
