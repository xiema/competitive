from sys import stdin,stdout
from collections import namedtuple
from bisect import bisect, bisect_left

Trap = namedtuple('Trap', ['loc','disarm','danger'])

m,n,k,t = map(int, stdin.readline().split())
squad = list(map(int, stdin.readline().split()))
traps = []
closest = n
for _ in range(k):
    l,r,d = map(int, stdin.readline().split())
    traps.append(Trap(l,r,d))
traps.sort(key=lambda trap : trap.disarm)
sorted = [trap.disarm for trap in traps]
avail = (t-n-1)/2
i = bisect(sorted, avail)

maxdanger = 0
while i < k:
    maxdanger = max(maxdanger, traps[i].danger)
    i+=1

squad.sort()
j = bisect_left(squad, maxdanger)

stdout.write('{}\n'.format(m-j))
