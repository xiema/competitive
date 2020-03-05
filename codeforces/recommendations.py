from sys import stdin,stdout
from heapq import merge

n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))
tlist = list(map(int, stdin.readline().split()))

adict = {}
for i,a in enumerate(alist):
    adict.setdefault(a, []).append(-tlist[i])

next,add = [],{}
total = 0
prev = None
for c in sorted(adict.keys()):
    if prev:
        l = min(len(next), c-prev)
        for i in range(1,l):
            add[i] = add.get(i,0) + next[i]
        next = next[l:] if l < len(next) else []
        total += l*sum(next)
    adict[c].sort()
    next = list(merge(next, adict[c]))
    prev = c
else:
    for i in range(1,len(next)):
        add[i] = add.get(i,0) + next[i]
    for i,v in add.items():
        total+=i*v

stdout.write(str(-total))
