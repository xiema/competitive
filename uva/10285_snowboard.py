from sys import stdin,stdout
from collections import deque

def lp(g, v, memo):
    if v in memo:
        return memo[v]
    l = 0
    for c in g[v]:
        l = max(l, lp(g,c,memo))
    l+=1
    memo[v] = l
    return l


N = int(stdin.readline().strip())

for _ in range(N):
    name,R,C = stdin.readline().split()
    R,C = int(R),int(C)

    M = []
    for _ in range(R):
        r = list(map(int, stdin.readline().split()))
        M.append(r)

    g = {}
    for i in range(R):
        for j in range(C):
            if (i,j) not in g:
                g[(i,j)] = set()
            if i > 0 and M[i][j] > M[i-1][j]:
                g[(i,j)].add((i-1,j))
            if i < R-1 and M[i][j] > M[i+1][j]:
                g[(i,j)].add((i+1,j))
            if j > 0 and M[i][j] > M[i][j-1]:
                g[(i,j)].add((i,j-1))
            if j < C-1 and M[i][j] > M[i][j+1]:
                g[(i,j)].add((i,j+1))

    l,memo = 0,{}
    for i in range(R):
        for j in range(C):
            l = max(l, lp(g, (i,j), memo))

    stdout.write('{}: {}\n'.format(name,l))
