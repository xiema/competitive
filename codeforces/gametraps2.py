from sys import stdin,stdout
from collections import deque
from bisect import bisect_left

m,n,k,t = map(int, stdin.readline().split())
soldiers = list(map(int, stdin.readline().split()))
dangers = []
points = []
for _ in range(k):
    l,r,d = map(int, stdin.readline().split())
    dangers.append(d)
    points.append((l, r, d))
soldiers.sort()
dangers.sort()
points.sort()

def gettime (d):
    total = 0
    cur = None
    for p in filter(lambda x: x[2] >= d, points):
        if not cur:
            total += p[1]-p[0]+1
            cur = p[1]
        else:
            if p[1] <= cur:
                continue
            else:
                if p[0] > cur:
                    total += p[1]-p[0]+1
                    cur = p[1]
                else:
                    total += p[1]-cur
                    cur = p[1]
    return total*2


t -= n+1
i,j = 0,k
minlevel = 0
while True:
    k = i + (j-i)//2
    if gettime(dangers[k]) > t:
        if i == k:
            minlevel = dangers[k]
            break
        else:
            i = k
    else:
        if j == k:
            if k == 0:
                minlevel = 0
            else:
                minlevel = dangers[k-1]
            break
        else:
            j = k

i = bisect_left(soldiers, minlevel)
stdout.write('{}\n'.format(m-i))
