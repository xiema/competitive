from sys import stdin,stdout
from collections import namedtuple
from bisect import bisect, bisect_left

Trap = namedtuple('Trap', ['loc','disarm','danger'])
m,n,k,t = map(int, stdin.readline().split())
soldiers = list(map(int, stdin.readline().split()))
traps = []
for _ in range(k):
    l,r,d = map(int, stdin.readline().split())
    traps.append(Trap(l,r,d))
soldiers.sort()
traps.sort(key = lambda x: x.danger, reverse = True)

t -= n+1
disarmed = []
minlevel = 0
for trap in traps:
    minlevel = trap.danger
    a,b = trap.loc,trap.disarm
    i = bisect(disarmed, (a,b))
    if i > 0 and a <= disarmed[i-1][1]:
        a,b = disarmed[i-1]
        t += 2*(b-a+1)
        b = max(b, trap.disarm)
        del disarmed[i-1]
        i-=1

    while i < len(disarmed):
        next = disarmed[i]
        if next[0] <= b:
            t += 2*(next[1]-next[0]+1)
            b = max(b, next[1])
            del disarmed[i]
        else:
            break
    t -= 2*(b-a+1)
    if t < 0:
        break
    disarmed.insert(i, (a,b))
else:
    minlevel = 0

i = bisect_left(soldiers, minlevel)
stdout.write('{}\n'.format(m-i))
