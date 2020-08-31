from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
R = {}
for _ in range(N-1):
    a,b = map(int, stdin.readline().split())
    R.setdefault(a, set()).add(b)
    R.setdefault(b, set()).add(a)

O = []
stk = deque([(1,0)])
while stk:
    u,p = stk.pop()
    O.append(u)
    for v in R[u]:
        if v==p:
            continue
        stk.append((v,u))

C = [0 for _ in range(N+1)]
for u in reversed(O):
