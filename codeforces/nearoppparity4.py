from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
ints = list(map(int, stdin.readline().split()))
counts = {0:{},1:{}}

nopp = {}
rpt = []
def get_nopp(i, p, seen):
    if p==ints[i]%2:
        return 0, False
    if i in nopp:
        return nopp[i], False
    if i in seen:
        rpt.append(i)
        return n, True

    seen.add(i)
    a,b = i-ints[i],i+ints[i]
    sa,sb = n,n
    ba,bb = False,False
    if a >= 0:
        sa,ba = get_nopp(a, p, seen)
    if b < n:
        sb,bb = get_nopp(b, p, seen)
    if ba or bb:
        rpt.append(i)

    c = min(sa,sb) + 1
    if c < n:
        nopp[i] = c
    return c, ba or bb

out = []
for i in range(n):
    print(i)
    rpt = []
    p = (ints[i]+1)%2
    get_nopp(i,p,set())
    for i in rpt:
        print(i)
        a,b = i-ints[i],i+ints[i]
        sa,sb = nopp[a] if a >=0 else n, nopp[b] if b < n else n
        nopp[i] = min(nopp[i], min(sa,sb))

for i in range(n):
    stdout.write("{} ".format(nopp[i] if nopp[i] < n else -1))
