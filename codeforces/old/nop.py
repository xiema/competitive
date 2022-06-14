from sys import stdin,stdout
from collections import deque
n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))

nop = {}
p = [set() for _ in range(n)]

def back(next):
    while next:
        i,c = next.popleft()
        if c < nop[i]:
            nop[i] = c
            c+=1
            for j in p[i]:
                next.append((j,c))

def bfs(x):
    if x not in nop:
        next = deque([x])
        pr = alist[x]%2
        nop[x] = n
        while next:
            i = next.popleft()
            for j in [i-alist[i],i+alist[i]]:
                if j >= 0 and j<n:
                    p[j].add(i)
                    if alist[j]%2!=pr:
                        back(deque([(i,1)]))
                    elif j in nop:
                        back(deque([(i,nop[j]+1)]))
                    else:
                        nop[j] = n
                        next.append(j)

    return nop[x] if nop[x]<n else -1

stdout.write(' '.join(str(bfs(x)) for x in range(n)))
