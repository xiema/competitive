from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())
nc = list(map(int, stdin.readline().split()))
T = [set() for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, stdin.readline().split())
    T[u].add(v)
    T[v].add(u)

F = {}
C = []
CR = {0 : 0}
O = []
rem,fix = set(),0
stk = deque()
def dfs(r):
    c0,c1 = 0,0
    stk.append((0, r, 0, 0))
    while stk:
        b,u,p,c = stk.pop()
        if u in F:
            continue
        F[u] = c
        O.append(u)
        if c:
            c1+=1
        else:
            c0+=1
        _c = (c+1)%2
        for v in T[u]:
            if v==p:
                continue
            if v in F:
                if F[v] == c:
                    return False
                continue
            stk.append((0, v, u, _c))

    if c0==c1:
        CR[r] = 0
        CR[0] += c0
    elif c0+c1==1:
        rem.add(r)
    else:
        C.append([c0,c1,r])
    return True

def solve(i, a):
    if i == len(C):
        return a>=0 and a <= len(rem)
    if solve(i+1, a-C[i][0]):
        CR[C[i][2]] = 0
        return True
    if solve(i+1, a-C[i][1]):
        CR[C[i][2]] = 1
        return True
    return False


for u in range(1,n+1):
    if u in F:
        continue
    if not dfs(u):
        print("NO")
        break
else:
    if solve(0, nc[1]-CR[0]):
        L = ['' for _ in range(n+1)]
        for i in O:
            if i in rem:
                continue
            if i in CR:
                cref = CR[i]
            if F[i]==cref:
                L[i] = '2'
                nc[1]-=1
            elif nc[0]:
                L[i] = '1'
                nc[0]-=1
            else:
                L[i] = '3'
                nc[2]-=1
        for i in rem:
            if nc[0]:
                L[i] = '1'
                nc[0]-=1
            elif nc[2]:
                L[i] = '3'
                nc[2]-=1
            else:
                L[i] = '2'

        print("YES")
        print(''.join(L))


    else:
        print("NO")
