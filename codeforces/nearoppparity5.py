from sys import stdin,stdout,setrecursionlimit
from collections import deque
setrecursionlimit(300000)
n = int(stdin.readline().strip())
alist = list(map(int,stdin.readline().split()))
nop = {}

class Graph():
    def __init__(self, n, alist):
        self.alist = alist
        self.n = n
        self.nop = {}
        self.parent = {}
        self.next = deque()

    def bfs(x):
        if x in self.nop:
            return nop[x]

        self.next.append(x)
        while self.next:


def bfs (x):
    p = alist[x]%2
    next = deque([(x,1)])
    parent = {}

    def bfs_aux(i,j,c):
        if j not in parent and j >= 0 and j < n:
            parent[j] = i
            if alist[j]%2!=p:
                return j, c
            else:
                next.append((j,c+1))

    y,yc = None,n
    while next:
        i,c = next.popleft()
        if c >= yc:
            break
        j = i-alist[i]
        if j in nop:
            y,yc =
        y,yc = bfs_aux(i,i-alist[i],c) or (y,yc)
        y,yc = bfs_aux(i,i+alist[i],c) or (y,yc)

    if y:
        if alist[y]%2!=p:
            y = parent[y]
            nop[y] = 1
        while y in parent:
            nop[parent[y]],y = nop[y]+1,parent[y]
        return nop[x]
    else:
        for i in parent:
            nop[i] = -1
        nop[x] = -1
        return -1

stdout.write(' '.join(str(bfs(x)) for x in range(n)))
