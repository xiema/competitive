from sys import stdin,stdout
from collections import deque

t = int(stdin.readline().strip())

for _ in range(t):
    n,k = map(int, stdin.readline().split())
    D,T = [0 for _ in range(n+1)],{}
    for _ in range(n-1):
        x,y = map(int, stdin.readline().split())
        D[x]+=1
        D[y]+=1
        T.setdefault(x, set()).add(y)
        T.setdefault(y, set()).add(x)

    L = [0 for _ in range(n+1)]
    q = deque()
    c = 0
    for i in range(1,n+1):
        if len(T[i]) == 1:
            for v in T[i]:
                L[v]+=1
                if L[v]==k:
                    q.append(v)
            D[i]=0

    while q:
        u = q.popleft()
        d = L[u]//k
        c += d
        d *= k
        L[u] -= d
        D[u] -= d
        if D[u] == 1:
            for v in T[u]:
                if D[v]>0:
                    L[v]+=1
                    if L[v]==k:
                        q.append(v)
                    break
            D[u] = 0

    ans = c

    stdout.write('{}\n'.format(ans))
